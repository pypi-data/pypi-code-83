import os


def _getCol(s):
    colours = {
        "str": "\033[92m",  # Green
        "int": "\033[96m",  # Cyan
        "bytes": "\033[94m",  # Blue
        "bytearray": "\033[64m",  # Dark blue
        "float": "\033[36m",  # Dark cyan
        "bool": "\033[93m",  # Yellow
        "list": "\033[91m",  # Red
        "dict": "\033[31m",  # Dark red
        "tuple": "\033[95m",  # Pink
        "set": "\033[35m"  # Dark pink
    }
    if str(type(s).__name__) in colours:
        return colours[str(type(s).__name__)]
    return "\033[0m"


def _basic(s, indent, show_types, colour_coded, debug):
    db = ""
    if isinstance(s, str):
        db = f" | Length: {len(s)}" if debug else ""
    return (" "*indent[1]) + _getCol(s) + (f"<{type(s).__name__}{db}> " if show_types else "") + str(s)


def _bytes(s, indent, show_types, colour_coded, debug):
    s = str(s)[2:-1] if isinstance(s, bytes) else str(s)[12:-2]
    return (" "*indent[1]) + _getCol(s) + (f"<{type(s).__name__}> " if show_types else "") + s


def _dict(s, indent, show_types, colour_coded, debug):
    indent[1] += indent[0]
    out = []
    for k, v in s.items():
        key = _process(k, indent, show_types, colour_coded, debug)[0]
        value = ("\n".join(_process(v, indent, show_types, colour_coded, debug))).strip()

        out.append(f"{key}: {value}")
    indent[1] -= indent[0]
    return out


def _list(s, indent, show_types, colour_coded, debug):
    indent[1] += indent[0]
    out = []
    for element in s:
        out.append("\n".join(_process(element, indent, show_types, colour_coded, debug)))
    indent[1] -= indent[0]
    return out


def _process(s, indent, show_types, colour_coded, debug):
    string = []
    if type(s) in [list, set, tuple, dict]:
        brackets = ["", ""]
        if type(s) in [list]:
            brackets = ["[", "]"]
        elif type(s) in [dict, set]:
            brackets = ["{", "}"]
        elif type(s) in [tuple]:
            brackets = ["(", ")"]
        i = (" "*indent[1]) or ""
        db = f" | Length: {len(s)}" if debug else ""
        t = f"<{type(s).__name__}{db}> " if show_types else ""
        string.append(i + _getCol(s) + f"{t}{brackets[0]}")
        if type(s) in [list, tuple, set]:
            string += _list(s, indent, show_types, colour_coded, debug)
        elif type(s) in [dict]:
            string += _dict(s, indent, show_types, colour_coded, debug)
        string.append(i + _getCol(s) + brackets[1])
    elif type(s) in [bytes, bytearray]:
        string.append(_bytes(s, indent, show_types, colour_coded, debug))
    else:
        string.append(_basic(s, indent, show_types, colour_coded, debug))
    return string


def pprint(data: any, indent: int = 4, show_types: bool = False, colour_coded: bool = True, cutoff: bool = True, debug: bool = False, return_string: bool = True):
    try:
        tw = int(os.popen('stty size', 'r').read().split()[1])
    except IndexError:
        cutoff = False
        tw = 1000000
    if isinstance(indent, int):
        indent = [indent, 0]
    if debug:
        show_types = True

    out = []
    parsed = []
    for line in _process(data, indent, show_types, colour_coded, debug):
        parsed += line.split("\n")
    for line in parsed:
        if len(line) > tw and cutoff:
            info = f"... [{len(line)}]"
            line = line[:tw-len(info)] + info
        out.append(line)
    if return_string:
        return ("\n".join(out) + ("\033[0m" if colour_coded else ""))
    print("\n".join(out) + ("\033[0m" if colour_coded else ""))
