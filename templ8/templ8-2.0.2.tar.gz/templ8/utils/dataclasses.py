import sys
from inspect import Parameter, signature
from typing import Any, Dict, List

from templ8.utils.dicts import merge_dicts, without


def dataclass_keys(cls: Any) -> List[str]:
    return list(signature(cls.__init__).parameters.keys())


def dataclass_defaults(cls: Any) -> Dict[str, Any]:
    return {
        k: annotation_default(v)
        for k, v in without(dict(signature(cls.__init__).parameters), "self").items()
        if v.default != Parameter.empty
    }


def filter_dataclass_input(cls: Any, dct: Dict[str, Any]) -> Dict[str, Any]:
    return dict(
        filter(
            lambda x: x[0] in dataclass_keys(cls),
            dct.items(),
        )
    )


def map_to_signature(cls: Any, dct: Dict[str, Any]) -> Dict[str, Any]:
    return merge_dicts(dataclass_defaults(cls), filter_dataclass_input(cls, dct))


def annotation_default(parameter: Parameter) -> Any:
    if str(parameter.default) != "<factory>":
        return parameter.default

    if sys.version_info > (3, 7, 0):
        factory_key = "__origin__"

    elif sys.version_info > (3, 6, 0):
        factory_key = "__extra__"

    else:
        raise NotImplementedError

    return getattr(parameter.annotation, factory_key)()
