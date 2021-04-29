"""Pretty printing of complex objects, borrowed from RLlib

https://github.com/ray-project/ray/blob/master/rllib/utils/debug.py

"""

import pprint
from typing import Mapping

import numpy as np
import torch

_printer = pprint.PrettyPrinter(indent=2, width=60)


def summarize(obj):
    """Return a pretty-formatted string for an object.
    This has special handling for pretty-formatting of commonly used data types
    in RLlib, such as SampleBatch, numpy arrays, etc.
    """

    return _printer.pformat(_summarize(obj))


def _summarize(obj):
    if isinstance(obj, Mapping):
        return {k: _summarize(v) for k, v in obj.items()}
    elif hasattr(obj, "_asdict"):
        return {
            "type": obj.__class__.__name__,
            "data": _summarize(obj._asdict()),
        }
    elif isinstance(obj, list):
        return [_summarize(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(_summarize(x) for x in obj)
    elif isinstance(obj, torch.Tensor):
        return _summarize(obj.cpu().detach().numpy())
    elif isinstance(obj, np.ndarray):
        if obj.size == 0:
            return _StringValue("np.ndarray({}, dtype={})".format(obj.shape, obj.dtype))
        elif obj.dtype == np.object or obj.dtype.type is np.str_:
            return _StringValue(
                "np.ndarray({}, dtype={}, head={})".format(
                    obj.shape, obj.dtype, _summarize(obj[0])
                )
            )
        else:
            return _StringValue(
                "np.ndarray({}, dtype={}, min={}, max={}, mean={})".format(
                    obj.shape,
                    obj.dtype,
                    round(float(np.min(obj)), 3),
                    round(float(np.max(obj)), 3),
                    round(float(np.mean(obj)), 3),
                )
            )
    else:
        return obj


class _StringValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value
