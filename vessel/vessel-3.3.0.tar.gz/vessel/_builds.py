import collections
import weakref
import itertools
import copy

from . import _share
from . import _updates
from . import _modifies


__all__ = ('Field', 'missing', 'update', 'build_vessel', 'build_list',
           'build_dict')


def _build(create, update, identify, cls):

    datas = weakref.WeakKeyDictionary()

    if identify:
        units = weakref.WeakValueDictionary()
    else:
        units = None

    class Unit(cls):

        __slots__ = ('__weakref__',)

        def __new__(cls, data, *args, unique = False, **kwargs):

            if identify and not unique:
                identity = identify(data)
                try:
                    self = units[identity]
                except KeyError:
                    forge = attach = True
                else:
                    forge = attach = False
            else:
                forge = True
                attach = False

            if forge:
                self = super().__new__(cls)
                if create:
                    datas[self] = create(data)

            if attach:
                units[identity] = self

            if update:
                _updates.any_(self, data)

            return self

        def __anycopy__(self, func):

            data = datas[self]

            fdata = func(data)

            fself = super().__new__(self.__class__)

            datas[fself] = fdata

            return fself

        def __copy__(self):

            func = lambda data: copy.copy(data)

            return self.__anycopy__(func)

        def __deepcopy__(self, memo):

            func = lambda data: copy.deepcopy(data, memo)

            return self.__anycopy__(func)

    return Unit, datas


def build(create, update, identify, add, pop, cls = object):

    Unit, datas = _build(create, update, identify, cls)

    context = _share.Context(Unit, update, datas, add, pop)

    _share.contexts.append(context)

    return Unit


def _get_data(unit):

    context = _share.get(unit.__class__)

    data = context.datas[unit]

    return data


missing = type(
    'missing',
    (),
    {
        '__slots__': (),
        '__bool__': False.__bool__,
        '__repr__': lambda self: '<missing>'
    }
)()


Field = collections.namedtuple(
    'Field',
    'type name make default factory',
    defaults = (None, None, None, missing, None)
)


def build_vessel(info, identify = None, cls = object, **behave):

    def create(data):

        root = {}

        return root

    def update(root, data, **kwargs):

        kwargs = {**behave, **kwargs}

        _updates.unit(info, root, data, **kwargs)

    names = {field.name: name for (name, field) in info.items() if field.name}

    pro_alias = lambda name: names.get(name, name)

    pre_alias = lambda name: info[name].name or name

    class Vessel(cls):

        __slots__ = ()

        def __getattr__(self, name):

            name = pro_alias(name)

            try:
                field = info[name]
            except KeyError as error:
                raise AttributeError(*error.args) from None

            if field.make:
                return field.make(self)

            context = _share.get(self.__class__)

            data = context.datas[self]

            value = data.get(name, field.default)

            if value is missing and field.factory:
                value = data[name] = field.factory()

            return value

        def __repr__(self):

            data = _get_data(self)

            names = data.keys()
            names = map(pre_alias, names)

            values = data.values()
            values = map(repr, values)

            items = zip(names, values)

            pairs = ', '.join(map('{0[0]}={0[1]}'.format, items))

            return '{0}({1})'.format(self.__class__.__name__, pairs)

    Unit = build(create, update, identify, None, None, Vessel)

    return Unit


def _method_data_proxy_wrap(name):

    def function(self, *args, **kwargs):

        data = _get_data(self)

        return getattr(data, name)(*args, **kwargs)

    return function


_collection_names = ('__iter__', '__len__', '__getitem__')


def _collection__repr__(self):

    data = _get_data(self)

    return '{0}({1})'.format(self.__class__.__name__, len(data))


def _collect(cls, names):

    space = {'__slots__': (), '__repr__': _collection__repr__}

    for name in itertools.chain(_collection_names, names):
        space[name] = _method_data_proxy_wrap(name)

    CollectionBase = type('CollectionBase', (cls,), space)

    return CollectionBase


def build_list(make, compare, cls = object, **behave):

    def create(data):

        root = []

        return root

    def update(root, data, **kwargs):

        kwargs = {**behave, **kwargs}

        _updates.list_(compare, make, root, data, **kwargs)

    def add(root, data):

        return _modifies.list_add(compare, make, root, data)

    def pop(root, data, key):

        return _modifies.list_pop(compare, root, data, key)

    CollectionBase = _collect(cls, ())

    Unit = build(create, update, None, add, pop, CollectionBase)

    class List(Unit):

        __slots__ = ()

    return List


def build_dict(make, identify, cls = object, **behave):

    def create(data):

        root = {}

        return root

    def update(root, data, **kwargs):

        kwargs = {**behave, **kwargs}

        _updates.dict_(identify, make, root, data, **kwargs)

    def add(root, data):

        return _modifies.dict_add(identify, make, root, data)

    def pop(root, data = missing, key = missing):

        return _modifies.dict_pop(identify, root, data, key)

    CollectionBase = _collect(cls, ('get', 'keys', 'values', 'items'))

    Unit = build(create, update, None, add, pop, CollectionBase)

    class Dict(Unit):

        __slots__ = ()

        def __iter__(self):

            yield from self.values()

    return Dict
