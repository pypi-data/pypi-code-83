import base64
import functools
import hashlib
import inspect
import logging
import re
import string
import time
import uuid
import warnings
from collections import OrderedDict
from importlib import import_module
from typing import Optional, Union, Callable, Any, Tuple, List

from .backends.base_cache import BaseCache

logger = logging.getLogger(__name__)

valid_chars = set(string.ascii_letters + string.digits + "_.")
del_chars = "".join(c for c in map(chr, range(256)) if c not in valid_chars)
null_control = (dict((k, None) for k in del_chars),)


def wants_args(f: Callable) -> bool:
    """Check if the function wants any arguments"""

    arg_spec = inspect.getfullargspec(f)

    return bool(arg_spec.args or arg_spec.varargs or arg_spec.varkw)


def get_arg_names(f: Callable) -> List[str]:
    """Return arguments of function

    :param f:
    :return: String list of arguments
    """
    sig = inspect.signature(f)
    return [
        parameter.name
        for parameter in sig.parameters.values()
        if parameter.kind == parameter.POSITIONAL_OR_KEYWORD
    ]


def get_arg_default(f: Callable, position: int):
    sig = inspect.signature(f)
    arg = list(sig.parameters.values())[position]
    arg_def = arg.default
    return arg_def if arg_def != inspect.Parameter.empty else None


def get_id(obj):
    return getattr(obj, "__caching_id__", repr)(obj)


def function_namespace(f, args=None):
    """Attempts to returns unique namespace for function"""
    m_args = get_arg_names(f)

    instance_token = None

    instance_self = getattr(f, "__self__", None)

    if instance_self and not inspect.isclass(instance_self):
        instance_token = get_id(f.__self__)
    elif m_args and m_args[0] == "self" and args:
        instance_token = get_id(args[0])

    module = f.__module__

    if m_args and m_args[0] == "cls" and not inspect.isclass(args[0]):
        raise ValueError(
            "When using `delete_memoized` on a "
            "`@classmethod` you must provide the "
            "class as the first argument"
        )

    if hasattr(f, "__qualname__"):
        name = f.__qualname__
    else:
        klass = getattr(f, "__self__", None)

        if klass and not inspect.isclass(klass):
            klass = klass.__class__

        if not klass:
            klass = getattr(f, "im_class", None)

        if not klass:
            if m_args and args:
                if m_args[0] == "self":
                    klass = args[0].__class__
                elif m_args[0] == "cls":
                    klass = args[0]

        if klass:
            name = klass.__name__ + "." + f.__name__
        else:
            name = f.__name__

    ns = ".".join((module, name))
    ns = ns.translate(*null_control)

    if instance_token:
        ins = ".".join((module, name, instance_token))
        ins = ins.translate(*null_control)
    else:
        ins = None

    return ns, ins


def _eval_string(template, pattern, context):
    groups = list(re.finditer(pattern, template))

    if groups:
        exp_value = eval(
            template[groups[0].start() + 2: groups[0].end() - 2], context
        )  # pylint: disable=eval-used
        template = (
                template[: groups[0].start()] + str(exp_value) + template[groups[0].end():]
        )
        return _eval_string(template, pattern, context)

    return template


class Cache:
    """This class is used to control the cache objects."""

    def __init__(self, config=None) -> None:
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        self.config = config

        self.source_check = None
        self.debug = False

        if config:
            self.init(config)

    def _set_cache(self, config) -> None:
        import_me = config["CACHE_TYPE"]
        backend = import_module("awesome_caching.backends")
        if "." in import_me:
            class_str = import_me.split(".")[-1]
            backend_str = import_me[:-len(class_str) - 1]
            backend = import_module(backend_str)
            import_me = class_str
        try:
            cache_factory = getattr(backend, import_me)
        except ImportError:
            from .backends import NullCache
            cache_factory = NullCache
            logger.error(
                f"Load cache factory error: cannot find {import_me}, no such backend"
            )
            if self.debug:
                raise

        cache_args = config["CACHE_ARGS"][:]
        cache_options = {"default_timeout": config["CACHE_DEFAULT_TIMEOUT"]}

        if isinstance(cache_factory, type) and issubclass(cache_factory, BaseCache):
            cache_factory = cache_factory.factory
        elif not callable(cache_factory):
            warnings.warn(
                "Using the initialization functions in awesome_caching.backend "
                "is deprecated.  Use the a full path to backend classes "
                "directly.",
                category=DeprecationWarning,
            )

        if config["CACHE_OPTIONS"]:
            cache_options.update(config["CACHE_OPTIONS"])
        self.cache = cache_factory(config, cache_args, cache_options)

    def init(self, config: dict):
        config.setdefault("CACHE_DEFAULT_TIMEOUT", 300)
        config.setdefault("CACHE_IGNORE_ERRORS", False)
        config.setdefault("CACHE_THRESHOLD", 500)
        config.setdefault("CACHE_KEY_PREFIX", "caching_")
        config.setdefault("CACHE_MEMCACHED_SERVERS", None)
        config.setdefault("CACHE_DIR", None)
        config.setdefault("CACHE_OPTIONS", None)
        config.setdefault("CACHE_ARGS", [])
        config.setdefault("CACHE_TYPE", "null")
        config.setdefault("CACHE_NO_NULL_WARNING", False)
        config.setdefault("CACHE_SOURCE_CHECK", False)

        if config["CACHE_TYPE"] == "null" and not config["CACHE_NO_NULL_WARNING"]:
            warnings.warn(
                "Awesome-Caching: CACHE_TYPE is set to null, caching is effectively disabled."
            )

        if config["CACHE_TYPE"] == "filesystem" and config["CACHE_DIR"] is None:
            warnings.warn(
                "Awesome-Caching: CACHE_TYPE is set to filesystem but no CACHE_DIR is set."
            )

        self.source_check = config["CACHE_SOURCE_CHECK"]
        self.debug = config.get("CACHE_DEBUG", False)
        self._set_cache(config)

    def get(self, *args, **kwargs) -> Optional[Union[str, dict]]:
        """Proxy function for internal cache object."""
        return self.cache.get(*args, **kwargs)

    def set(self, *args, **kwargs) -> bool:
        """Proxy function for internal cache object."""
        return self.cache.set(*args, **kwargs)

    def add(self, *args, **kwargs) -> bool:
        """Proxy function for internal cache object."""
        return self.cache.add(*args, **kwargs)

    def delete(self, *args, **kwargs) -> bool:
        """Proxy function for internal cache object."""
        return self.cache.delete(*args, **kwargs)

    def delete_many(self, *args, **kwargs) -> bool:
        """Proxy function for internal cache object."""
        return self.cache.delete_many(*args, **kwargs)  # type: ignore

    def clear(self) -> None:
        """Proxy function for internal cache object."""
        return self.cache.clear()

    def get_many(self, *args, **kwargs):
        """Proxy function for internal cache object."""
        return self.cache.get_many(*args, **kwargs)

    def set_many(self, *args, **kwargs):
        """Proxy function for internal cache object."""
        return self.cache.set_many(*args, **kwargs)

    def get_dict(self, *args, **kwargs):
        """Proxy function for internal cache object."""
        return self.cache.get_dict(*args, **kwargs)

    def unlink(self, *args, **kwargs) -> bool:
        """Proxy function for internal cache object
        only support Redis
        """
        unlink = getattr(self.cache, "unlink", None)
        if unlink is not None and callable(unlink):
            return unlink(*args, **kwargs)
        return self.delete_many(*args, **kwargs)

    def cached(
            self,
            timeout: Optional[int] = None,
            key_prefix: Union[str, Callable] = "caching/%s",
            unless: Optional[Callable] = None,
            forced_update: Optional[Callable] = None,
            hash_method: Callable = hashlib.md5,
            cache_none: bool = False,
            make_cache_key: Optional[Callable] = None,
            source_check: Optional[bool] = None,
    ) -> Callable:
        """Decorator. Use this to cache a function. By default the cache key
        is `caching/request.path`. You are able to use this decorator with any
        function by changing the `key_prefix`. If the token `%s` is located
        within the `key_prefix` then it will replace that with `request.path`

        Example::

            # An example view function
            @cache.cached(timeout=50)
            def big_foo():
                return big_bar_calc()

            # An example misc function to cache.
            @cache.cached(key_prefix='MyCachedList')
            def get_list():
                return [random.randrange(0, 1) for i in range(50000)]

            my_list = get_list()

        .. note::

            You MUST have a request context to actually called any functions
            that are cached.

        :param timeout: Default None. If set to an integer, will cache for that
                        amount of time. Unit of time is in seconds.

        :param key_prefix: Default 'caching/%(request.path)s'. Beginning key to .
                           use for the cache key. `request.path` will be the
                           actual request path, or in cases where the
                           `make_cache_key`-function is called from other
                           views it will be the expected URL for the view
                           as generated by Awesome's `url_for()`.

        :param unless: Default None. Cache will *always* execute the caching
                       facilities unless this callable is true.
                       This will bypass the caching entirely.

        :param forced_update: Default None. If this callable is true,
                              cache value will be updated regardless cache
                              is expired or not. Useful for background
                              renewal of cached functions.

        :param hash_method: Default hashlib.md5. The hash method used to
                            generate the keys for cached results.
        :param cache_none: Default False. If set to True, add a key exists
                           check when cache.get returns None. This will likely
                           lead to wrongly returned None values in concurrent
                           situations and is not recommended to use.
        :param make_cache_key: Default None. If set to a callable object,
                           it will be called to generate the cache key

        :param source_check: Default None. If None will use the value set by
                             CACHE_SOURCE_CHECK.
                             If True, include the function's source code in the
                             hash to avoid using cached values when the source
                             code has changed and the input values remain the
                             same. This ensures that the cache_key will be
                             formed with the function's source code hash in
                             addition to other parameters that may be included
                             in the formation of the key.
        """

        def decorator(f):
            @functools.wraps(f)
            def decorated_function(*args, **kwargs):
                #: Bypass the cache entirely.
                if self._bypass_cache(unless, f, *args, **kwargs):
                    return f(*args, **kwargs)

                nonlocal source_check
                if source_check is None:
                    source_check = self.source_check

                try:
                    if make_cache_key is not None and callable(make_cache_key):
                        cache_key = make_cache_key(*args, **kwargs)
                    else:
                        cache_key = _make_cache_key(args, kwargs)

                    if (
                            callable(forced_update)
                            and (
                            forced_update(*args, **kwargs)
                            if wants_args(forced_update)
                            else forced_update()
                    )
                            is True
                    ):
                        rv = None
                        found = False
                    else:
                        rv = self.cache.get(cache_key)
                        found = True

                        # If the value returned by cache.get() is None, it
                        # might be because the key is not found in the cache
                        # or because the cached value is actually None
                        if rv is None:
                            # If we're sure we don't need to cache None values
                            # (cache_none=False), don't bother checking for
                            # key existence, as it can lead to false positives
                            # if a concurrent call already cached the
                            # key between steps. This would cause us to
                            # return None when we shouldn't
                            if not cache_none:
                                found = False
                            else:
                                found = self.cache.has(cache_key)
                except Exception:
                    if self.debug:
                        raise
                    logger.exception("Exception possibly due to cache backend.")
                    return f(*args, **kwargs)

                if not found:
                    rv = f(*args, **kwargs)

                    try:
                        self.cache.set(
                            cache_key,
                            rv,
                            timeout=decorated_function.cache_timeout,
                        )
                    except Exception:
                        if self.debug:
                            raise
                        logger.exception("Exception possibly due to cache backend.")
                return rv

            def default_make_cache_key(*args, **kwargs):
                # Convert non-keyword arguments (which is the way
                # `make_cache_key` expects them) to keyword arguments
                # (the way `url_for` expects them)
                arg_spec_args = inspect.getfullargspec(f).args

                for arg_name, arg in zip(arg_spec_args, args):
                    kwargs[arg_name] = arg

                return _make_cache_key(args, kwargs)

            def _make_cache_key(args, kwargs):
                if callable(key_prefix):
                    cache_key = key_prefix()
                else:
                    cache_key = key_prefix

                if source_check and callable(f):
                    func_source_code = inspect.getsource(f)
                    func_source_hash = hash_method(func_source_code.encode("utf-8"))
                    func_source_hash = str(func_source_hash.hexdigest())

                    cache_key += func_source_hash

                return cache_key

            decorated_function.uncached = f
            decorated_function.cache_timeout = timeout
            decorated_function.make_cache_key = default_make_cache_key

            return decorated_function

        return decorator

    @staticmethod
    def _memvname(func_name: str) -> str:
        return func_name + "_memver"

    @staticmethod
    def _memoize_make_version_hash() -> str:
        return base64.b64encode(uuid.uuid4().bytes)[:6].decode("utf-8")

    def _memoize_version(
            self,
            f: Callable,
            args: Optional[Any] = None,
            kwargs=None,
            reset: bool = False,
            delete: bool = False,
            timeout: Optional[int] = None,
            forced_update: Optional[Union[bool, Callable]] = False,
            args_to_ignore: Optional[Any] = None,
            dependencies: Optional[List[str]] = None,
    ) -> Union[Tuple[str, str], Tuple[str, None]]:
        """Updates the hash version associated with a memoized function or
        method.
        """
        fname, instance_fname = function_namespace(f, args=args)
        version_key = self._memvname(fname)
        fetch_keys = [version_key]

        args_to_ignore = args_to_ignore or []
        if "self" in args_to_ignore:
            instance_fname = None

        if instance_fname:
            instance_version_key = self._memvname(instance_fname)
            fetch_keys.append(instance_version_key)

        # Only delete the per-instance version key or per-function version
        # key but not both.
        if delete:
            self.cache.delete_many(fetch_keys[-1])
            return fname, None

        version_data_list = list(self.cache.get_many(*fetch_keys))
        dirty = False

        if (
                callable(forced_update)
                and (
                forced_update(*(args or ()), **(kwargs or {}))
                if wants_args(forced_update)
                else forced_update()
        )
                is True
        ):
            # Mark key as dirty to update its TTL
            dirty = True

        if version_data_list[0] is None:
            version_data_list[0] = self._memoize_make_version_hash()
            dirty = True

        if instance_fname and version_data_list[1] is None:
            version_data_list[1] = self._memoize_make_version_hash()
            dirty = True

        # Only reset the per-instance version or the per-function version
        # but not both.
        if reset:
            fetch_keys = fetch_keys[-1:]
            version_data_list = [self._memoize_make_version_hash()]
            dirty = True

        if dirty:
            self.cache.set_many(
                dict(zip(fetch_keys, version_data_list)), timeout=timeout
            )

        version_data = "".join(version_data_list)
        if dependencies:
            version_data += self._get_cache_deps(dependencies, f, args)
        return fname, version_data

    def _get_cache_deps(self, dependencies, f, args):
        cache_dep_keys = self._get_cache_dep_keys(dependencies, f, args)
        cache_dep_versions = self.cache.get_many(*cache_dep_keys)

        now = str(time.time())
        versions = []

        for cache_key, existing_version in zip(cache_dep_keys, cache_dep_versions):
            version_to_use = existing_version

            while not version_to_use:
                if self.cache.set(cache_key, now):
                    version_to_use = now
                else:
                    version_to_use = self.get(cache_key)

            if isinstance(version_to_use, bytes):
                versions.append(version_to_use.decode("ascii"))
            else:
                versions.append(version_to_use)

        return ":" + "_".join(versions)

    def _get_cache_dep_keys(self, dependencies, f, args):
        cache_keys = []

        arg_names = [
            parameter.name for parameter in inspect.signature(f).parameters.values()
        ]
        context = dict(zip(arg_names, args))

        for dep in dependencies:
            dep = dep.strip()

            if context:
                dep_key = _eval_string(dep, "{{.*?}}", context)
            else:
                dep_key = dep
            cache_keys.append("{}{}:version".format(self.cache.key_prefix, dep_key))
        return cache_keys

    def _memoize_make_cache_key(
            self,
            make_name: None = None,
            timeout: Optional[Callable] = None,
            forced_update: Optional[Union[bool, Callable]] = False,
            hash_method: Callable = hashlib.md5,
            source_check: Optional[bool] = False,
            args_to_ignore: Optional[Any] = None,
            dependencies: Optional[List[str]] = None,
    ) -> Callable:
        """Function used to create the cache_key for memoized functions."""

        def make_cache_key(f, *args, **kwargs):
            _timeout = getattr(timeout, "cache_timeout", timeout)
            fname, version_data = self._memoize_version(
                f,
                args=args,
                kwargs=kwargs,
                timeout=_timeout,
                forced_update=forced_update,
                args_to_ignore=args_to_ignore,
                dependencies=dependencies,
            )

            #: this should have to be after version_data, so that it
            #: does not break the delete_memoized functionality.
            altfname = make_name(fname) if callable(make_name) else fname

            if callable(f):
                key_args, key_kwargs = self._memoize_kwargs_to_args(
                    f, *args, **kwargs, args_to_ignore=args_to_ignore
                )
            else:
                key_args, key_kwargs = args, kwargs

            updated = "{0}{1}{2}".format(altfname, key_args, key_kwargs)

            cache_key = hash_method()
            cache_key.update(updated.encode("utf-8"))

            # Use the source code if source_check is True and update the
            # cache_key with the function's source.
            if source_check and callable(f):
                func_source_code = inspect.getsource(f)
                cache_key.update(func_source_code.encode("utf-8"))

            cache_key = base64.b64encode(cache_key.digest())[:16]
            cache_key = cache_key.decode("utf-8")
            cache_key += version_data

            return cache_key

        return make_cache_key

    @staticmethod
    def _memoize_kwargs_to_args(f: Callable, *args, **kwargs) -> Any:
        #: Inspect the arguments to the function
        #: This allows the memoization to be the same
        #: whether the function was called with
        #: 1, b=2 is equivalent to a=1, b=2, etc.
        new_args = []
        arg_num = 0
        args_to_ignore = kwargs.pop("args_to_ignore", None) or []

        # If the function uses VAR_KEYWORD type of parameters,
        # we need to pass these further
        kw_keys_remaining = list(kwargs.keys())
        arg_names = get_arg_names(f)
        args_len = len(arg_names)

        for i in range(args_len):
            arg_default = get_arg_default(f, i)
            if arg_names[i] in args_to_ignore:
                arg = None
                arg_num += 1
            elif i == 0 and arg_names[i] in ("self", "cls"):
                #: use the id func of the class instance
                #: this supports instance methods for
                #: the memoized functions, giving more
                #: flexibility to developers
                arg = get_id(args[0])
                arg_num += 1
            elif arg_names[i] in kwargs:
                arg = kwargs[arg_names[i]]
                kw_keys_remaining.pop(kw_keys_remaining.index(arg_names[i]))
            elif arg_num < len(args):
                arg = args[arg_num]
                arg_num += 1
            elif arg_default:
                arg = arg_default
                arg_num += 1
            else:
                arg = None
                arg_num += 1

            new_args.append(arg)

        new_args.extend(args[len(arg_names):])
        return (
            tuple(new_args),
            OrderedDict(
                sorted((k, v) for k, v in kwargs.items() if k in kw_keys_remaining)
            ),
        )

    @staticmethod
    def _bypass_cache(unless: Optional[Callable], f: Callable, *args, **kwargs) -> bool:
        """Determines whether or not to bypass the cache by calling unless().
        Supports both unless() that takes in arguments and unless()
        that doesn't.
        """
        bypass_cache = False

        if callable(unless):
            arg_spec = inspect.getfullargspec(unless)
            has_args = len(arg_spec.args) > 0 or arg_spec.varargs or arg_spec.varkw

            # If unless() takes args, pass them in.
            if has_args:
                if unless(f, *args, **kwargs) is True:
                    bypass_cache = True
            elif unless() is True:
                bypass_cache = True

        return bypass_cache

    def memoize(
            self,
            timeout: Optional[int] = None,
            make_name: None = None,
            unless: None = None,
            forced_update: Optional[Callable] = None,
            hash_method: Callable = hashlib.md5,
            cache_none: bool = False,
            source_check: Optional[bool] = None,
            args_to_ignore: Optional[Any] = None,
            dependencies: Optional[List[str]] = None,
    ) -> Callable:
        """Use this to cache the result of a function, taking its arguments
        into account in the cache key.

        Information on
        `Memoization <http://en.wikipedia.org/wiki/Memoization>`_.

        Example::
                @cache.memoize(timeout=50)
                def big_foo(a, b):
                    return a + b + random.randrange(0, 1000)

        .. code-block:: pycon

            >>> big_foo(5, 2)
            753
            >>> big_foo(5, 3)
            234
            >>> big_foo(5, 2)
            753

        :param timeout: Default None. If set to an integer, will cache for that
                        amount of time. Unit of time is in seconds.
        :param make_name: Default None. If set this is a function that accepts
                          a single argument, the function name, and returns a
                          new string to be used as the function name.
                          If not set then the function name is used.
        :param unless: Default None. Cache will *always* execute the caching
                       facilities unless this callable is true.
                       This will bypass the caching entirely.
        :param forced_update: Default None. If this callable is true,
                              cache value will be updated regardless cache
                              is expired or not. Useful for background
                              renewal of cached functions.
        :param hash_method: Default hashlib.md5. The hash method used to
                            generate the keys for cached results.
        :param cache_none: Default False. If set to True, add a key exists
                           check when cache.get returns None. This will likely
                           lead to wrongly returned None values in concurrent
                           situations and is not recommended to use.

        :param source_check: Default None. If None will use the value set by
                             CACHE_SOURCE_CHECK.
                             If True, include the function's source code in the
                             hash to avoid using cached values when the source
                             code has changed and the input values remain the
                             same. This ensures that the cache_key will be
                             formed with the function's source code hash in
                             addition to other parameters that may be included
                             in the formation of the key.
        :param args_to_ignore: List of arguments that will be ignored while
                               generating the cache key. Default to None.
                               This means that those arguments may change
                               without affecting the cache value that will be
                               returned.
        :param dependencies: Dependency cache keys
        """

        def memoize(f):
            @functools.wraps(f)
            def decorated_function(*args, **kwargs):
                #: bypass cache
                if self._bypass_cache(unless, f, *args, **kwargs):
                    return f(*args, **kwargs)

                nonlocal source_check
                if source_check is None:
                    source_check = self.source_check

                try:
                    cache_key = decorated_function.make_cache_key(f, *args, **kwargs)

                    if (
                            callable(forced_update)
                            and (
                            forced_update(*args, **kwargs)
                            if wants_args(forced_update)
                            else forced_update()
                    )
                            is True
                    ):
                        rv = None
                        found = False
                    else:
                        rv = self.cache.get(cache_key)
                        found = True

                        # If the value returned by cache.get() is None, it
                        # might be because the key is not found in the cache
                        # or because the cached value is actually None
                        if rv is None:
                            # If we're sure we don't need to cache None values
                            # (cache_none=False), don't bother checking for
                            # key existence, as it can lead to false positives
                            # if a concurrent call already cached the
                            # key between steps. This would cause us to
                            # return None when we shouldn't
                            if not cache_none:
                                found = False
                            else:
                                found = self.cache.has(cache_key)
                except Exception:
                    logger.exception("Exception possibly due to cache backend.")
                    if self.debug:
                        raise
                    return f(*args, **kwargs)

                if not found:
                    rv = f(*args, **kwargs)

                    try:
                        self.cache.set(
                            cache_key,
                            rv,
                            timeout=decorated_function.cache_timeout,
                        )
                    except Exception:
                        logger.exception("Exception possibly due to cache backend.")
                        if self.debug:
                            raise
                return rv

            decorated_function.uncached = f
            decorated_function.cache_timeout = timeout
            decorated_function.make_cache_key = self._memoize_make_cache_key(
                make_name=make_name,
                timeout=decorated_function,
                forced_update=forced_update,
                hash_method=hash_method,
                source_check=source_check,
                args_to_ignore=args_to_ignore,
                dependencies=dependencies,
            )
            decorated_function.delete_memoized = lambda: self.delete_memoized(f)

            return decorated_function

        return memoize

    def delete_memoized(self, f, *args, **kwargs) -> None:
        """Deletes the specified functions caches, based by given parameters.
        If parameters are given, only the functions that were memoized
        with them will be erased. Otherwise all versions of the caches
        will be forgotten.

        Example::

            @cache.memoize(50)
            def random_func():
                return random.randrange(1, 50)

            @cache.memoize()
            def param_func(a, b):
                return a+b+random.randrange(1, 50)

        .. code-block:: pycon

            >>> random_func()
            43
            >>> random_func()
            43
            >>> cache.delete_memoized(random_func)
            >>> random_func()
            16
            >>> param_func(1, 2)
            32
            >>> param_func(1, 2)
            32
            >>> param_func(2, 2)
            47
            >>> cache.delete_memoized(param_func, 1, 2)
            >>> param_func(1, 2)
            13
            >>> param_func(2, 2)
            47

        Delete memoized is also smart about instance methods vs class methods.

        When passing a instancemethod, it will only clear the cache related
        to that instance of that object. (object uniqueness can be overridden
        by defining the __repr__ method, such as user id).

        When passing a classmethod, it will clear all caches related across
        all instances of that class.

        Example::

            class Adder(object):
                @cache.memoize()
                def add(self, b):
                    return b + random.random()

        .. code-block:: pycon

            >>> adder1 = Adder()
            >>> adder2 = Adder()
            >>> adder1.add(3)
            3.23214234
            >>> adder2.add(3)
            3.60898509
            >>> cache.delete_memoized(adder1.add)
            >>> adder1.add(3)
            3.01348673
            >>> adder2.add(3)
            3.60898509
            >>> cache.delete_memoized(Adder.add)
            >>> adder1.add(3)
            3.53235667
            >>> adder2.add(3)
            3.72341788

        :param f: The memoized function.
        :param args: A list of positional parameters used with
                       memoized function.
        :param kwargs: A dict of named parameters used with
                          memoized function.

        .. note::

            Awesome-Caching uses inspect to order kwargs into positional args when
            the function is memoized. If you pass a function reference into
            ``fname``, Awesome-Caching will be able to place the args/kwargs in
            the proper order, and delete the positional cache.

            However, if ``delete_memoized`` is just called with the name of the
            function, be sure to pass in potential arguments in the same order
            as defined in your function as args only, otherwise Awesome-Caching
            will not be able to compute the same cache key and delete all
            memoized versions of it.

        .. note::

            Awesome-Caching maintains an internal random version hash for
            the function. Using delete_memoized will only swap out
            the version hash, causing the memoize function to recompute
            results and put them into another key.

            This leaves any computed caches for this memoized function within
            the caching backend.

            It is recommended to use a very high timeout with memoize if using
            this function, so that when the version hash is swapped, the old
            cached results would eventually be reclaimed by the caching
            backend.
        """
        if not callable(f):
            raise TypeError(
                "Deleting messages by relative name is not supported, please "
                "use a function reference."
            )

        if not (args or kwargs):
            self._memoize_version(f, reset=True)
        else:
            cache_key = f.make_cache_key(f.uncached, *args, **kwargs)
            self.cache.delete(cache_key)

    def delete_memoized_verhash(self, f: Callable, *args) -> None:
        """Delete the version hash associated with the function.

        .. warning::

            Performing this operation could leave keys behind that have
            been created with this version hash. It is up to the application
            to make sure that all keys that may have been created with this
            version hash at least have timeouts so they will not sit orphaned
            in the cache backend.
        """
        if not callable(f):
            raise TypeError(
                "Deleting messages by relative name is not supported, please"
                "use a function reference."
            )

        self._memoize_version(f, delete=True)
