import json
from typing import Optional, TypeVar

from mindfoundry.client.horizon.generated.types import Response

SomeType = TypeVar("SomeType")


class ApiError(RuntimeError):
    def __init__(self, message: str, ref: str):
        super().__init__(message)
        self._ref = ref

    @property
    def ref(self) -> str:
        return self._ref


def non_optional(value: Optional[SomeType]) -> SomeType:
    assert value is not None
    return value


def assert_success(response: Response[SomeType]) -> None:
    if response.status_code < 200 or response.status_code >= 300:
        content = json.loads(response.content)
        if "summary" in content and "ref" in content:
            raise ApiError(content["summary"], content["ref"])
        else:
            raise RuntimeError(f"Unknown api error. Status code {response.status_code}")


def return_value_or_raise_error(response: Response[SomeType]) -> SomeType:
    assert_success(response)
    return non_optional(response.parsed)
