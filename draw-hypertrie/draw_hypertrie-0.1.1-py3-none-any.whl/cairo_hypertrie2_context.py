import math
from collections import OrderedDict
from typing import List, Tuple, Union, Dict

import cairo
from cairo import Context

from hypertrie.colors import *
from hypertrie.hypertrie2 import HypertrieContext, hash_t, HypertrieNode


class PlotStyle:
    """
    Defines styles for plot
    """

    def __init__(self,
                 padding=8,
                 hpadding=None,
                 block_size=25,
                 corner_radius=None,
                 dim_tag_size=None,
                 line_width=2,
                 font_size=None,
                 ):
        self.padding = padding

        if hpadding is None:
            self.hpadding = self.padding / 2
        else:
            self.hpadding = hpadding

        self.block_size = block_size

        if dim_tag_size is None:
            self.dim_tag_size = self.block_size / 25 * 15
        else:
            self.dim_tag_size = dim_tag_size

        if corner_radius is None:
            self.corner_radius = self.block_size / 5
        else:
            self.corner_radius = corner_radius

        self.line_width = line_width

        if font_size is None:
            self.font_size = self.block_size / 25 * 15
        else:
            self.font_size = font_size

        self.dim_font_size = self.dim_tag_size / 25 * 19

        self.sb_padding = self.padding + self.line_width / 2
        self.db_padding = self.padding + self.line_width
        self.sb_hpadding = self.hpadding + self.line_width / 2
        self.db_hpadding = self.hpadding + self.line_width

        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def rounded_rectangle(ctx: Context,
                      x: float, y: float,
                      width, height,
                      fill_color=light_gray_transp,
                      border_color=None,
                      aspect=1.0,
                      corner_radius=None):
    if corner_radius is None:
        corner_radius = height / 10

    from math import pi
    radius = corner_radius / aspect
    degrees = pi / 180.0

    ctx.new_sub_path()
    ctx.arc(x + width - radius, y + radius, radius, -90 * degrees, 0 * degrees)
    ctx.arc(x + width - radius, y + height - radius, radius, 0 * degrees, 90 * degrees)
    ctx.arc(x + radius, y + height - radius, radius, 90 * degrees, 180 * degrees)
    ctx.arc(x + radius, y + radius, radius, 180 * degrees, 270 * degrees)
    ctx.close_path()

    ctx.set_source_rgba(*fill_color)
    if border_color is None:
        ctx.fill()
    else:
        ctx.fill_preserve()
        ctx.set_source_rgba(*border_color)
        ctx.stroke()


def arrow(ctx: Context, ps: PlotStyle,
          start_x, start_y,
          end_x, end_y,
          color=black, head_length=4):
    head_degree = 0.6
    angle = math.atan2(end_y - start_y, end_x - start_x) + math.pi

    x1 = end_x + head_length * math.cos(angle - head_degree)
    y1 = end_y + head_length * math.sin(angle - head_degree)
    x2 = end_x + head_length * math.cos(angle + head_degree)
    y2 = end_y + head_length * math.sin(angle + head_degree)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    # rectangle

    ctx.set_line_width(ps.line_width)
    ctx.set_source_rgba(*color)

    ctx.new_sub_path()
    ctx.move_to(end_x, end_y)
    ctx.line_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.line_to(end_x, end_y)
    ctx.close_path()
    ctx.fill()

    ctx.move_to(xm, ym)
    ctx.line_to(start_x, start_y)
    ctx.stroke()


def rect_with_text(ctx: Context, ps: PlotStyle,
                   x: float,
                   y: float,
                   text,
                   size: float,
                   rgba_border=black,
                   rgba_font=black,
                   rgba_fill=(0, 0, 0, 0)):
    # rectangle
    size = float(size)
    ctx.set_line_width(ps.line_width)
    ctx.set_font_size(size / 25 * 19)

    ctx.rectangle(x, y, size, size)
    if rgba_fill is not None:
        ctx.set_source_rgba(*rgba_fill)
        ctx.fill_preserve()
    ctx.set_source_rgba(*rgba_border)
    ctx.stroke()

    # text
    (x_, y_, width, height, dx, dy) = ctx.text_extents(str(text))
    (ascent, descent, height, max_x_advance, max_y_advance) = ctx.font_extents()

    ctx.move_to(x + (size / 2) - dx / 2, y + (size / 2) + ((ascent - descent) / 2))
    ctx.set_source_rgba(*rgba_font)
    ctx.show_text(str(text))


class DimBox:

    def dim_font_height(self):
        self.ctx.set_font_size(self.ps.dim_font_size)
        (ascent, descent, font_height, max_x_advance, max_y_advance) = self.ctx.font_extents()
        return (ascent - descent)

    def __init__(self, ctx: Context, ps: PlotStyle, x: float, y: float, data, dim: int, n_dim: int):
        self.ctx = ctx
        self.ps = ps
        self.x = x
        self.y = y

        self.font_height = self.dim_font_height()
        self.arrow_dx = self.ps.block_size / 2
        self.arrow_length = self.ps.line_width * 3

        self.data = data
        self.dim = dim
        self.n_dim = n_dim
        self.width = len(data) * self.ps.block_size + (len(data) + 1) * self.ps.db_hpadding
        self.height = self.ps.sb_hpadding + self.dim_font_height() + self.ps.sb_hpadding + \
                      +self.ps.block_size + \
                      (self.n_dim > 1) * (self.ps.block_size + self.arrow_length + self.ps.line_width / 2) + \
                      +  self.ps.db_hpadding

    def draw(self):
        # draw background
        rounded_rectangle(self.ctx, self.x, self.y,
                          width=self.width,
                          height=self.height,
                          fill_color=desert_sand,
                          border_color=white,
                          corner_radius=self.ps.corner_radius
                          )

        # draw dim x text
        dx = self.ps.db_hpadding
        text = f"dim {self.dim}"
        self.ctx.set_font_size(self.ps.dim_font_size)
        self.ctx.move_to(self.x + dx, self.y + self.ps.sb_hpadding + self.dim_font_height())
        self.ctx.set_source_rgba(*white)
        self.ctx.show_text(text)

        # draw mapping
        for (key_part, value) in self.data:
            dy = self.ps.sb_hpadding + self.dim_font_height() + self.ps.sb_hpadding
            rect_with_text(self.ctx, self.ps, self.x + dx, self.y + dy,
                           text=key_part,
                           size=self.ps.block_size,
                           rgba_border=white,
                           rgba_font=white,
                           rgba_fill=dark_grey_blue
                           )
            if self.n_dim > 1:
                dy += self.ps.block_size
                arrow_start = (self.x + dx + self.arrow_dx, self.y + dy)
                arrow_tip = (arrow_start[0], arrow_start[1] + self.arrow_length)
                arrow(self.ctx, self.ps, *arrow_start, *arrow_tip, color=white, head_length=2 * self.ps.line_width)

                dy += self.arrow_length + self.ps.line_width / 2
                rect_with_text(self.ctx, self.ps, self.x + dx, self.y + dy,
                               text=value,
                               size=self.ps.block_size,
                               rgba_border=white,
                               rgba_font=white,
                               rgba_fill=dark_grey_blue if type(value) is int else light_persian_green
                               )
            dx += self.ps.block_size + self.ps.db_hpadding


def add_referencable_hypertrie_node(ctx: Context, ps: PlotStyle, x: float, y: float,
                                    id: str, ref_count: int, size: int,
                                    data: Union[List[List[Tuple[Union[int, str], Union[int, str]]]],
                                                List[int]], node: HypertrieNode
                                    ):
    rect_with_text(ctx, ps, x + ps.corner_radius, y,
                   text=id,
                   size=ps.block_size,
                   rgba_border=dark_gray,
                   rgba_fill=persian_green,
                   rgba_font=white)
    y_offset = ps.block_size + .5 * ps.line_width
    arrow_start = (x + ps.corner_radius + ps.block_size / 2, y + y_offset)
    arrow_tip = (arrow_start[0], arrow_start[1] + ps.line_width * 2.5)
    arrow(ctx, ps, *arrow_start, *arrow_tip, color=dark_gray_transp, head_length=2 * ps.line_width)
    y_offset += ps.line_width * 2.5
    node_x, node_y = x, y + y_offset
    assert (isinstance(data, list) and len(data) != 0 and isinstance(data[0], int)) == (size == 1)
    if size == 1:

        asset = CompressedHypertrieNode(ctx, ps, node_x, node_y,
                                        id=id,
                                        ref_count=ref_count,
                                        size=size,
                                        data=data)
    else:
        asset = UncomressedHypertrieNode(ctx, ps, node_x, node_y,
                                         id=id,
                                         ref_count=ref_count,
                                         size=size,
                                         data=data)

    asset.draw()

    return asset.width, asset.height + y_offset


class AbsctractNode:
    pass


class UncomressedHypertrieNode:

    def text_widths(self, ref_count, size):
        self.ctx.set_font_size(self.ps.font_size)
        ascent, descent, font_height, max_x_advance, max_y_advance = self.ctx.font_extents()
        ref_text = f"{ref_count}"
        size_text = f"{size}"
        r_width = self.ctx.text_extents(str("r:")).x_advance
        z_width = self.ctx.text_extents(str("z:")).x_advance
        ref_width = self.ctx.text_extents(ref_text).x_advance
        size_width = self.ctx.text_extents(size_text).x_advance
        whitespace_width = self.ctx.text_extents(" ").x_advance
        pre_width = max(r_width, z_width)
        post_width = max(ref_width, size_width)
        return pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height

    def __init__(self, ctx: Context, ps: PlotStyle, x: float, y: float, id: str, ref_count: int, size, data):
        self.ctx = ctx
        self.ps = ps
        self.id = id
        self.ref_count = ref_count
        self.data = data
        self.n_dim = len(data)
        self.size = size
        self.x = x
        self.y = y

        dy = self.ps.sb_padding
        dx = self.ps.sb_padding

        max_dim_box_height = 0

        self.dim_boxes = list()
        for dim, dim_data in enumerate(self.data, 1):
            dim_box = DimBox(self.ctx,
                             self.ps,
                             self.x + dx,
                             self.y + dy,
                             n_dim=self.n_dim,
                             dim=dim,
                             data=dim_data)

            dim_box_width, dim_box_height = dim_box.width, dim_box.height
            self.dim_boxes.append(dim_box)

            max_dim_box_height = max(max_dim_box_height, dim_box_height)

            dx += dim_box_width + self.ps.db_hpadding

        self.mapping_dx = dx

        self.height = dy + max_dim_box_height + self.ps.sb_padding

        pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height = self.text_widths(
            self.ref_count, self.size)

        self.width = self.mapping_dx + pre_width + whitespace_width + post_width + self.ps.padding

    def draw(self):
        rounded_rectangle(self.ctx, self.x, self.y, self.width, self.height, corner_radius=self.ps.corner_radius)

        for dim_box in self.dim_boxes:
            dim_box.draw()

        pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height = self.text_widths(
            self.ref_count, self.size)

        text_dy = font_height + self.ps.corner_radius
        self.ctx.set_source_rgba(*dark_gray)
        self.ctx.move_to(self.x + self.mapping_dx + (pre_width - r_width), self.y + text_dy)
        self.ctx.show_text("r:")
        self.ctx.move_to(self.x + self.mapping_dx + pre_width + whitespace_width + (post_width - ref_width),
                         self.y + text_dy)
        self.ctx.show_text(ref_text)

        text_dy += font_height
        self.ctx.move_to(self.x + self.mapping_dx + (pre_width - z_width), self.y + text_dy)
        self.ctx.show_text("z:")
        self.ctx.move_to(self.x + self.mapping_dx + pre_width + whitespace_width + (post_width - size_width),
                         self.y + text_dy)
        self.ctx.show_text(size_text)


class CompressedHypertrieNode:

    def text_widths(self, ref_count, size):
        self.ctx.set_font_size(self.ps.font_size)
        ascent, descent, font_height, max_x_advance, max_y_advance = self.ctx.font_extents()
        ref_text = f"{ref_count}"
        size_text = f"{size}"
        r_width = self.ctx.text_extents(str("r:")).x_advance
        z_width = self.ctx.text_extents(str("z:")).x_advance
        ref_width = self.ctx.text_extents(ref_text).x_advance
        size_width = self.ctx.text_extents(size_text).x_advance
        whitespace_width = self.ctx.text_extents(" ").x_advance
        pre_width = max(r_width, z_width)
        post_width = max(ref_width, size_width)
        return pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height

    def __init__(self, ctx: Context, ps: PlotStyle, x: float, y: float, id: str, ref_count: int, size, data):
        self.ctx = ctx
        self.ps = ps
        self.id = id
        self.ref_count = ref_count
        self.data = data
        self.n_dim = len(data)
        self.size = size
        self.x = x
        self.y = y

        self.mapping_dx = self.ps.sb_padding + self.ps.block_size + self.ps.sb_hpadding

        self.height = self.ps.sb_padding + self.ps.block_size * self.n_dim + self.ps.sb_padding

        pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height = self.text_widths(
            self.ref_count, self.size)

        self.width = self.mapping_dx + pre_width + whitespace_width + post_width + self.ps.padding

    def draw(self):
        rounded_rectangle(self.ctx, self.x, self.y, self.width, self.height, corner_radius=self.ps.corner_radius)

        dx = self.ps.sb_padding
        dy = self.ps.sb_padding

        for key_part in self.data:
            rect_with_text(self.ctx, self.ps, self.x + dx, self.y + dy,
                           text=key_part,
                           size=self.ps.block_size,
                           rgba_border=white,
                           rgba_font=white,
                           rgba_fill=dark_grey_blue
                           )
            dy += self.ps.block_size

        pre_width, whitespace_width, post_width, r_width, z_width, ref_width, size_width, ref_text, size_text, font_height = self.text_widths(
            self.ref_count, self.size)

        text_dy = font_height + self.ps.corner_radius
        self.ctx.set_source_rgba(*dark_gray)
        self.ctx.move_to(self.x + self.mapping_dx + (pre_width - r_width), self.y + text_dy)
        self.ctx.show_text("r:")
        self.ctx.move_to(self.x + self.mapping_dx + pre_width + whitespace_width + (post_width - ref_width),
                         self.y + text_dy)
        self.ctx.show_text(ref_text)

        text_dy += font_height
        self.ctx.move_to(self.x + self.mapping_dx + (pre_width - z_width), self.y + text_dy)
        self.ctx.show_text("z:")
        self.ctx.move_to(self.x + self.mapping_dx + pre_width + whitespace_width + (post_width - size_width),
                         self.y + text_dy)
        self.ctx.show_text(size_text)


def cairo_draw_hypertrie2_context(ctx: Context, ps: PlotStyle, ht_ctx: HypertrieContext):
    ctx.select_font_face("Liberation Sans", cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(ps.font_size)
    ctx.set_line_width(ps.line_width)

    node: HypertrieNode
    next_hash2id = OrderedDict()

    next_id = "A"

    def inc_id():
        nonlocal next_id
        next_id = chr(ord(next_id) + 1)

    def map_id(child: Union[int, hash_t]) -> str:
        nonlocal next_hash2id
        if type(child) is hash_t:
            if child not in next_hash2id:
                next_hash2id[child] = next_id
                inc_id()
            return next_hash2id[child]
        else:
            return child

    depth = 3
    nodes: Dict[hash_t, HypertrieNode] = ht_ctx.storage[depth - 1]
    x = 0
    y = ps.line_width / 2
    x_max = x
    x_offset = 0
    y_offset = 0
    for node_hash, node in nodes.items():
        id = next_id
        inc_id()

        data = [list() for _ in range(depth)]
        for dim in range(depth):
            entries = sorted(node.children[dim].items())

            data[dim] = [(key_part, map_id(child)) for key_part, child in entries]

        tmp_x_offset, y_offset = add_referencable_hypertrie_node(ctx, ps,
                                                                 x + x_offset, y,
                                                                 id=id,
                                                                 size=node.size,
                                                                 ref_count=node.count,
                                                                 data=data,
                                                                 node=node)
        x_offset += tmp_x_offset + 15
    y_offset += 15
    x_max = max(x_max, x + x_offset)
    ####
    depth = 2
    x_offset = 0
    y += y_offset
    y_offset = 0
    hash2id = next_hash2id.copy()
    next_hash2id.clear()
    nodes: Dict[hash_t, HypertrieNode] = ht_ctx.storage[depth - 1]
    assert len(nodes) == len(hash2id)
    for node_hash, id in hash2id.items():
        node = nodes[node_hash]

        data = [list() for _ in range(depth)]
        if node.size == 1:
            data = list(node.children)
        else:
            for dim in range(depth):
                entries = sorted(node.children[dim].items())

                data[dim] = [(key_part, map_id(child)) for key_part, child in entries]

        tmp_x_offset, tmp_y_offset = add_referencable_hypertrie_node(
            ctx, ps, x + x_offset, y,
            id=id,
            size=node.size,
            ref_count=node.count,
            data=data,
            node=node)
        x_offset += tmp_x_offset + 15
        y_offset = max(tmp_y_offset, y_offset)
    y_offset += 15
    x_max = max(x_max, x + x_offset)
    ####
    depth = 1
    y += y_offset
    y_offset = 0
    x_offset = 0
    hash2id = next_hash2id.copy()
    next_hash2id.clear()
    nodes: Dict[hash_t, HypertrieNode] = ht_ctx.storage[depth - 1]
    assert len(nodes) == len(hash2id)
    for node_hash, id in hash2id.items():
        node = nodes[node_hash]

        data = [list() for _ in range(depth)]
        assert node.size != 1

        for dim in range(depth):
            entries = sorted(node.children[dim])

            data[dim] = [(key_part, "") for key_part in entries]

        tmp_x_offset, tmp_y_offset = add_referencable_hypertrie_node(
            ctx, ps, x + x_offset, y,
            id=id,
            size=node.size,
            ref_count=node.count,
            data=data,
            node=node)
        x_offset += tmp_x_offset + 15
        y_offset = max(tmp_y_offset, y_offset)
    x_max = max(x_max, x + x_offset)
    x_max -= 15
    return x_max, y + y_offset

#
# ht_ctx = HypertrieContext()
# ht_ctx.create_hypertrie(
#     keys=[
#         (1, 2, 3),
#         (1, 2, 4),
#         (5, 2, 4),
#         (5, 2, 3),
#     ]
# )
# ht_ctx.create_hypertrie(
#     keys=[
#         (1, 2, 3),
#         (1, 2, 4),
#         (3, 2, 4),
#         (3, 2, 5),
#         (4, 2, 3),
#         (4, 2, 5),
#         (3, 6, 7),
#         (5, 6, 7),
#
#     ]
# )
#
# draw_hypertrie2_context(ht_ctx)
