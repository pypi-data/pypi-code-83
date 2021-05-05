import warnings


def pre(hub, ctx):
    warnings.warn(
        "pop-conf sub is deprecated, use pop-config", DeprecationWarning, stacklevel=2
    )
