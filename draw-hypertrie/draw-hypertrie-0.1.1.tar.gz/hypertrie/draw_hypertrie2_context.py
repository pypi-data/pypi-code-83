from typing import Optional

from hypertrie.cairo_hypertrie2_context import PlotStyle
from hypertrie.hypertrie2 import HypertrieContext


def draw_hypertrie2_context(ht_ctx: HypertrieContext, name: Optional[str] = None, ps: Optional[PlotStyle] = None):
    if ps is None:
        ps = PlotStyle()
    if name is None:
        import random
        name = "hypertrie2_plot_{}".format(random.randint(0, 10 ** 10))

    tmp_file = f"{name}.tmp.pdf"
    import cairo
    from hypertrie.cairo_hypertrie2_context import cairo_draw_hypertrie2_context
    with cairo.PDFSurface(tmp_file, 500, 500) as surf_tmp:
        ctx = cairo.Context(surf_tmp)
        max_x, max_y = cairo_draw_hypertrie2_context(ctx, ps, ht_ctx)
    from pathlib import Path
    Path(tmp_file).unlink()
    from math import ceil
    max_x = ceil(max_x)
    max_y = ceil(max_y)

    with cairo.PDFSurface(f"{name}.pdf", max_x, max_y) as surf_pdf:
        ctx = cairo.Context(surf_pdf)
        cairo_draw_hypertrie2_context(ctx, ps, ht_ctx)
        ctx.save()

    with cairo.SVGSurface(f"{name}.svg", max_x, max_y) as surf_svg:
        ctx = cairo.Context(surf_svg)
        cairo_draw_hypertrie2_context(ctx, ps, ht_ctx)
        ctx.save()

    scale_png = 4
    with cairo.ImageSurface(cairo.FORMAT_ARGB32, max_x * scale_png, max_y * scale_png) as surf_png:
        surf_png.set_device_scale(scale_png, scale_png)
        ctx = cairo.Context(surf_png)

        cairo_draw_hypertrie2_context(ctx, ps, ht_ctx)
        ctx.save()
        surf_png.flush()

        surf_png.write_to_png(f"{name}.png")
