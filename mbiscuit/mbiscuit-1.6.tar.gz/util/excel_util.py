import xlwt


def get_default_style():
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.bottom_colour = 0x3A

    # 对齐方式
    align = xlwt.Alignment()
    align.horz = 2

    # 样式加载对齐方式
    style = xlwt.XFStyle()
    style.borders = borders
    style.alignment = align
    return style
