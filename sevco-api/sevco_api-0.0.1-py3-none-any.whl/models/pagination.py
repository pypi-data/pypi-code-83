from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Pagination")


@attr.s(auto_attribs=True)
class Pagination:
    """ """

    page: float
    per_page: float
    total: float

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        per_page = self.per_page
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "page": page,
                "per_page": per_page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        pagination = cls(
            page=page,
            per_page=per_page,
            total=total,
        )

        return pagination
