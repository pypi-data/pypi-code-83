from collections import namedtuple


RGBA = namedtuple('RGBA', ['r', 'g', 'b', 'a'])
Palette = namedtuple('Palette', 'colors')

loaders = {}
savers = {}
extension_checkers = {}

def create(from_: str, to: str, width: int, height: int, path: str, output: str):
    if not from_:
        for handler, checker in extension_checkers.items():
            if checker(path):
                from_ = handler
                break
    
    if not to:
        for handler, checker in extension_checkers.items():
            if checker(output):
                to = handler
                break

    colors = loaders[from_](path)
    savers[to](width, height, colors, output)

def rgb_dict_to_tuple(d: dict) -> (float, float, float, float):
    return RGBA(d['r'], d['g'], d['b'], d.get('a') or 1)

def RGBA_to_hex(rgba: RGBA) -> str:
    r = int(float(rgba.r) * 255)
    g = int(float(rgba.g) * 255)
    b = int(float(rgba.b) * 255)
    try:
        a = int(float(rgba.a) * 255)
        return f'#{r:02x}{g:02x}{b:02x}{a:02x}'
    except KeyError:
        return f'#{r:02x}{g:02x}{b:02x}'

def RGBA_to_rgb_tuple(rgba: RGBA) -> str:
    r = int(float(rgba.r) * 255)
    g = int(float(rgba.g) * 255)
    b = int(float(rgba.b) * 255)
    return (r, g, b)