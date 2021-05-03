def build_from_cfg(cfg, registry):
    """Build a instance from config dict.

    Args:
        cfg (dict): Config dict. It should contain the key `type`.
        registry (Registry): The registry containing the `type`.

    Return:
        obj: The constructed object.
    """
    if not isinstance(cfg, dict):
        raise TypeError(f'cfg should be dict, but got {type(cfg)}')
    if 'type' not in cfg:
        raise KeyError(f'cfg should contain the key `type`, but got {cfg}')
    if not isinstance(registry, Registry):
        raise TypeError(
            f'registry should be Registry, but got {type(registry)}')

    args = cfg.copy()
    obj_type = args.pop('type')
    if isinstance(obj_type, str):
        obj_cls = registry.get(obj_type)
        if obj_cls is None:
            raise KeyError(
                f'Key {obj_type} is not in registry {registry.name}')
    else:
        raise TypeError(f'obj_type should be str, but got {type(obj_type)}')

    try:
        return obj_cls(**args)
    except Exception as e:
        raise type(e)(f'{obj_cls.__name__}: {e}')


class Registry:
    """The registry maps string to object.

    Example:
        >>> MODELS = Registry('models')
        >>> @MODELS.register()
        >>> class ResNet:
        >>>     pass
        >>> resnet = MODELS.get('ResNet')
        >>> model = MODELS.build({'type': 'ResNet'})

    Args:
        name (str): Registry name.
        build_func (func, optional): A function to build an instance
            from the registry based on a single dict argument.

    """

    # pylint: disable=R1710

    def __init__(self, name, build_func=None):
        self._name = name
        self._obj_map = {}

        if build_func is None:
            self.build_func = build_from_cfg
        else:
            self.build_func = build_func

    def _do_register(self, name, obj):
        if name in self._obj_map:
            raise KeyError(f'{name} is registered in registry {self._name}')
        self._obj_map[name] = obj

    def register(self, obj=None):
        """Register an object with its name `obj.__name__`.

        Can be called as a decorator or function.

        Example:
            >>> @MODELS.register()
            >>> class ResNet:
            >>>     pass
            >>> # or call it as a function
            >>> MODELS.register(ResNet)
        """
        if obj is None:
            # as a decorator
            def deco(func_or_class):
                name = func_or_class.__name__
                self._do_register(name, func_or_class)
                return func_or_class

            return deco

        # as a function
        name = obj.__name__
        self._do_register(name, obj)

    def get(self, name):
        """Return an object if it's registered, else None."""
        ret = self._obj_map.get(name)
        return ret

    def build(self, *args, **kwargs):
        """Build an object from the registry based on args."""
        return self.build_func(*args, **kwargs, registry=self)

    @property
    def name(self):
        """Get registry name"""
        return self._name

    def __len__(self):
        return len(self._obj_map)

    def __getitem__(self, name):
        ret = self._obj_map.get(name)
        if ret is None:
            raise KeyError(f'Key {name} is not in registry {self._name}')
        return ret

    def __setitem__(self, name, obj):
        raise NotImplementedError('Registry does not support item assignment')

    def __contains__(self, name):
        return name in self._obj_map

    def __repr__(self):
        fmt_str = f'Registry: {self._name}\nItems: {self._obj_map.items()}'
        return fmt_str
