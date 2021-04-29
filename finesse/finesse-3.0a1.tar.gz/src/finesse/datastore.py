"""Finesse datastore tools.

The datastore is intended for objects that should be cached during the execution of the
current Python kernel. Code typically uses this instead of the more bug-prone singleton
pattern (see #260).
"""

_DATASTORE = {}


def invalidate(key=None):
    """Invalidate the datastore.

    Parameters
    ----------
    key : str, optional
        The datastore key to invalidate.
    """
    if key is None:
        _DATASTORE.clear()
    else:
        del _DATASTORE[key]


def init_singleton(cls, *args, **kwargs):
    """Instantiate `cls` and return the object for the current and future calls.

    Parameters
    ----------
    cls : type
        The singeton class to retrieve. If `cls` has already been instantiated, the
        existing instance is returned and `args` and `kwargs` are ignored.

    Other Parameters
    ----------------
    args, kwargs
        Positional and keyword arguments to pass to the `cls` call, if `cls` is not yet
        instantiated.

    Returns
    -------
    object
        The instantiated singleton.
    """
    if cls not in _DATASTORE:
        _DATASTORE[cls] = cls(*args, **kwargs)
    return _DATASTORE[cls]


def has_singleton(cls):
    """Determine if `cls` is instantiated.

    Parameters
    ----------
    cls : type
        The singeton class to check.

    Returns
    -------
    bool
        `True` if an instance exists, `False` otherwise.
    """
    return cls in _DATASTORE


def invalidate_singleton(cls):
    """Invalidate a singleton object with type `cls`.

    Parameters
    ----------
    cls : type
        The singeton class to invalidate.
    """
    invalidate(cls)
