
from . import _share


__all__ = ('add', 'pop')


_marker = object()


def list_add(compare, build, root, data):

    present = True

    for value in root:
        if not compare(value, data):
            continue
        break
    else:
        present = False

    if not present:
        value = build(data)
        root.append(value)

    return (value, present)


def list_pop(compare, root, data, index):

    if index is _marker:
        present = any(compare(value, data) for value in root)
    else:
        present = index < len(data)

    if present:
        value = root.pop(index)
    else:
        value = None

    return (value, present)


def dict_add(identify, build, root, data):

    present = True

    identity = identify(data)

    try:
        value = root[identity]
    except KeyError:
        present = False

    if not present:
        value = build(data)
        root[identity] = value

    return (value, present)


def dict_pop(identify, root, data, identity):

    if identity is _marker:
        identity = identify(data)

    present = identity in root.keys()

    if present:
        value = root.pop(identity)
    else:
        value = None

    return (value, present)


def _any_do(add, value, *args, **kwargs):

    context = _share.get(value.__class__)

    root = context.datas[value]

    func = context.add if add else context.pop

    return func(root, *args, **kwargs)


def any_add(value, data):

    return _any_do(True, value, data)


def any_pop(value, *, data = _marker, key = _marker):

    return _any_do(False, value, data, key)
