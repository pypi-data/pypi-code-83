from math import ceil
import torch
import torch.nn.functional as F
from torch import nn, einsum

from einops import rearrange, repeat, reduce

# rotary

class SinusoidalEmbeddings(nn.Module):
    def __init__(self, dim):
        super().__init__()
        inv_freq = 1. / (10000 ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer('inv_freq', inv_freq)

    def forward(self, x):
        n = x.shape[-2]
        t = torch.arange(n, device = x.device).type_as(self.inv_freq)
        freqs = torch.einsum('i , j -> i j', t, self.inv_freq)
        emb = torch.cat((freqs, freqs), dim=-1)
        return emb[None, :, :]

def rotate_half(x):
    x = x.reshape((x.shape[0], -1, 2, x.shape[-1] // 2))
    x1, x2 = x.unbind(dim = -2)
    return torch.cat((-x2, x1), dim = -1)

def apply_rotary_pos_emb(q, k, freqs):
    q, k = map(lambda t: (t * freqs.cos()) + (rotate_half(t) * freqs.sin()), (q, k))
    return q, k

# helpers

def exists(val):
    return val is not None

def default(val, d):
    return val if exists(val) else d

def pad_to_multiple(tensor, multiple, dim = -1, value = 0):
    seqlen = tensor.shape[dim]
    m = seqlen / multiple
    if m.is_integer():
        return tensor
    remainder = ceil(m) * multiple - seqlen
    pad_offset = (0,) * (-1 - dim) * 2
    return F.pad(tensor, (*pad_offset, 0, remainder), value = value)

# helper classes

class Residual(nn.Module):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def forward(self, x, **kwargs):
        return self.fn(x, **kwargs) + x

class PreNorm(nn.Module):
    def __init__(self, dim, fn):
        super().__init__()
        self.fn = fn
        self.norm = nn.LayerNorm(dim)

    def forward(self, x, **kwargs):
        x = self.norm(x)
        return self.fn(x, **kwargs)

def FeedForward(dim, mult = 4):
    return nn.Sequential(
        nn.Linear(dim, dim * mult),
        nn.GELU(),
        nn.Linear(dim * mult, dim)
    )

class Attention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, causal = True):
        super().__init__()
        inner_dim = heads * dim_head
        self.heads = heads
        self.causal = causal
        self.scale = dim_head ** -0.5

        self.to_q = nn.Linear(dim, inner_dim, bias = False)
        self.to_kv = nn.Linear(dim, inner_dim * 2, bias = False)
        self.to_out = nn.Linear(inner_dim, dim)

    def forward(self, x, mask = None, context = None, with_self = False):
        h, device, has_context = self.heads, x.device, exists(context)
        context = default(context, x)

        if has_context and with_self:
            context = torch.cat((x, context), dim = 1)

        qkv = (self.to_q(x), *self.to_kv(context).chunk(2, dim = -1))
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> (b h) n d', h = h), qkv)

        sim = einsum('b i d, b j d -> b i j', q, k) * self.scale

        mask_value = -torch.finfo(sim.dtype).max

        if exists(mask):
            mask = rearrange(mask, 'b j -> b () j')
            sim.masked_fill_(~mask, mask_value)

        if self.causal:
            i, j = sim.shape[-2:]
            mask = torch.ones(i, j, device = device).triu_(j - i + 1).bool()
            mask = rearrange(mask, 'i j -> () i j')
            sim.masked_fill_(mask, mask_value)

        attn = sim.softmax(dim = -1)

        out = einsum('b i j, b j d -> b i d', attn, v)
        out = rearrange(out, '(b h) n d -> b n (h d)', h = h)
        return self.to_out(out)

class LocalAttention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, causal = True, window_size = 128):
        super().__init__()
        inner_dim = heads * dim_head
        self.heads = heads
        self.causal = causal
        self.scale = dim_head ** -0.5
        self.window_size = window_size

        self.to_q = nn.Linear(dim, inner_dim, bias = False)
        self.to_kv = nn.Linear(dim, inner_dim * 2, bias = False)
        self.to_out = nn.Linear(inner_dim, dim)

    def forward(
        self,
        x,
        mask = None,
        global_tokens = None,
        pos_emb = None
    ):
        h, device, w = self.heads, x.device, self.window_size

        b, n, *_ = x.shape
        x = pad_to_multiple(x, w, dim = -2, value = 0.)

        is_padded = x.shape[-2] != n

        qkv = (self.to_q(x), *self.to_kv(x).chunk(2, dim = -1))
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> (b h) n d', h = h), qkv)

        if exists(pos_emb):
            q, k = apply_rotary_pos_emb(q, k, pos_emb)

        window_fn = lambda t: rearrange(t, 'b (w n) d -> b w n d', n = w)
        q, k, v = map(window_fn, (q, k, v))

        k, v = map(lambda t: F.pad(t, (0, 0, 0, 0, 1, 0)), (k, v))
        k, v = map(lambda t: torch.cat((k[:, :-1], k[:, 1:]), dim = 2), (k, v))

        local_j = k.shape[-2]
        global_j = 0

        if exists(global_tokens):
            global_tokens = global_tokens[:, :-1] # last global token will never be attended to

            gk, gv = self.to_kv(global_tokens).chunk(2, dim = -1)
            gk, gv = map(lambda t: repeat(t, 'b n (h d) -> (b h) w n d', h = h, w = q.shape[1]), (gk, gv))

            k = torch.cat((gk, k), dim = -2)
            v = torch.cat((gv, v), dim = -2)

            global_j = gk.shape[-2]

        sim = einsum('b w i d, b w j d -> b w i j', q, k) * self.scale
        buckets, i, j = sim.shape[-3:]

        mask_value = -torch.finfo(sim.dtype).max

        if exists(mask) or is_padded:
            mask = default(mask, torch.ones((b, x.shape[-2]), device = device).bool())
            mask = pad_to_multiple(mask, w, dim = -1, value = False)
            mask = rearrange(mask, 'b (w n) -> b w () n', n = w)
            mask = F.pad(mask, (j - mask.shape[-1], 0), value = True)
            sim.masked_fill_(~mask, mask_value)

        if self.causal:
            mask = torch.ones(i, local_j, device = device).triu_(local_j - i + 1).bool()
            mask = repeat(mask, 'i j -> () u i j', u = buckets)

            if global_j > 0:
                global_mask = torch.ones(buckets, global_j, device = device).triu_(global_j - buckets + 1).bool()
                global_mask = repeat(global_mask, 'u j -> () u i j', i = i)
                mask = torch.cat((global_mask, mask), dim = -1)

            sim.masked_fill_(mask, mask_value)

        attn = sim.softmax(dim = -1)

        out = einsum('b w i j, b w j d -> b w i d', attn, v)
        out = rearrange(out, '(b h) w n d -> b (w n) (h d)', h = h)
        out = self.to_out(out[:, :n])
        return out

# main class

class Transformer(nn.Module):
    def __init__(
        self,
        *,
        num_tokens,
        dim,
        max_seq_len,
        depth,
        causal = True,
        dim_head = 64,
        heads = 8
    ):
        super().__init__()
        self.max_seq_len = max_seq_len

        self.token_emb = nn.Embedding(num_tokens, dim)
        self.pos_emb = nn.Embedding(max_seq_len, dim)

        self.layers = nn.ModuleList([])
        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                Residual(PreNorm(dim, Attention(dim, causal = causal, dim_head = dim_head, heads = heads))),
                Residual(PreNorm(dim, FeedForward(dim))),
            ]))

        self.to_logits = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_tokens)
        )

    def forward(self, x, mask = None):
        b, n, device = *x.shape, x.device

        x = self.token_emb(x)
        x += self.pos_emb(torch.arange(n, device = device))

        for attn, ff in self.layers:
            x = attn(x, mask = mask)
            x = ff(x)

        return self.to_logits(x)

# poolformer

class Poolformer(nn.Module):
    def __init__(
        self,
        *,
        num_tokens,
        dim,
        max_seq_len,
        depth,
        causal = True,
        dim_head = 64,
        heads = 8,
        window_size = 128,
        global_attn = True,
        global_tokens = True
    ):
        super().__init__()
        self.max_seq_len = max_seq_len
        self.window_size = window_size

        self.token_emb = nn.Embedding(num_tokens, dim)
        self.pos_emb = SinusoidalEmbeddings(dim_head)

        self.global_tokens = global_tokens
        self.global_pos_emb = nn.Embedding(ceil(max_seq_len / window_size), dim)

        self.global_transformer = nn.ModuleList([
            Residual(PreNorm(dim, Attention(dim))),
            Residual(PreNorm(dim, FeedForward(dim)))
        ]) if global_attn else None

        self.layers = nn.ModuleList([])
        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                Residual(PreNorm(dim, LocalAttention(dim, causal = causal, dim_head = dim_head, heads = heads, window_size = window_size))),
                Residual(PreNorm(dim, FeedForward(dim))),
            ]))

        self.to_logits = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_tokens)
        )

    def forward(self, x, mask = None):
        b, n, w, device = *x.shape, self.window_size, x.device

        x = self.token_emb(x)

        # mean pool tokens

        r = n % w
        xl, xr = x[:, :(n - r)], x[:, (n - r):]
        g = reduce(xl, 'b (w n) d -> b w d', 'mean', n = w)

        if r > 0:
            pooled_r = rearrange(xr.mean(dim = 1), 'b d -> b () d')
            g = torch.cat((g, pooled_r), dim = 1)

        # pos embedding

        pos_emb = self.pos_emb(x)
        global_pos_emb = self.global_pos_emb(torch.arange(ceil(n / w), device = device))

        g += rearrange(global_pos_emb, 'n d -> () n d')

        # layers

        for attn, ff in self.layers:

            if exists(self.global_transformer):
                global_attn, global_ff = self.global_transformer
                u = g.shape[-2]

                padded_x = pad_to_multiple(x, w, dim = -2, value = 0.)
                padded_x = rearrange(padded_x, 'b (u w) d -> (b u) w d', w = w)

                g = rearrange(g, 'b u d -> (b u) () d')
                g = global_attn(g, context = padded_x, with_self = True)
                g = rearrange(g, '(b u) () d -> b u d', u = u)

                g = global_ff(g)

            global_tokens = (g if self.global_tokens else None)

            x = attn(x, mask = mask, global_tokens = global_tokens, pos_emb = pos_emb)
            x = ff(x)

        # to logits

        return self.to_logits(x)
