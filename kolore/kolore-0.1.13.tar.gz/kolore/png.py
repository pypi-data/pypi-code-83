import kolore.palette as palette
from PIL import Image, ImageDraw


def save_png(width: int, height: int, colors: [palette.RGBA], output: str):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    num_colors = len(colors)
    color_width = width / num_colors
    for i, color in enumerate(colors):
        hex_name = palette.RGBA_to_tuple(color)
        draw.rectangle([(color_width * i, 0), (color_width * (i + 1), height)], fill=hex_name)
    
    img.save(output)

palette.savers['png'] = save_png
palette.extension_checkers['png'] = lambda f: f.endswith('.png')
