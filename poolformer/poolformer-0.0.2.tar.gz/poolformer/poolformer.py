from math import ceil
import torch
import torch.nn.functional as F
from torch import nn, einsum

from einops import rearrange, repeat, reduce

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

        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)
        self.to_out = nn.Linear(inner_dim, dim)

    def forward(self, x, mask = None):
        h, device = self.heads, x.device

        qkv = self.to_qkv(x).chunk(3, dim = -1)
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
        global_tokens = None
    ):
        h, device, w = self.heads, x.device, self.window_size

        b, n, *_ = x.shape
        x = pad_to_multiple(x, w, dim = -2, value = 0.)

        is_padded = x.shape[-2] != n

        qkv = (self.to_q(x), *self.to_kv(x).chunk(2, dim = -1))
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> (b h) n d', h = h), qkv)

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
                global_mask = torch.ones(buckets, global_j, device = device).triu_(global_j - i).bool()
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
        self.pos_emb = nn.Embedding(max_seq_len, dim)

        self.global_tokens = global_tokens
        self.global_pos_emb = nn.Embedding(ceil(max_seq_len / window_size), dim)

        self.global_transformer = nn.Sequential(
            Residual(PreNorm(dim, Attention(dim, causal = causal))),
            Residual(PreNorm(dim, FeedForward(dim)))
        ) if global_attn else None

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

        pos_emb = self.pos_emb(torch.arange(n, device = device))
        global_pos_emb = self.global_pos_emb(torch.arange(ceil(n / w), device = device))

        x += rearrange(pos_emb, 'n d -> () n d')
        g += rearrange(global_pos_emb, 'n d -> () n d')

        # layers

        for attn, ff in self.layers:

            if exists(self.global_transformer):
                g = self.global_transformer(g)

            global_tokens = (g if self.global_tokens else None)

            x = attn(x, mask = mask, global_tokens = global_tokens)
            x = ff(x)

        # to logits

        return self.to_logits(x)
