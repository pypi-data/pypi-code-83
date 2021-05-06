from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.device import Device
from ..models.pagination import Pagination

T = TypeVar("T", bound="DeviceResults")


@attr.s(auto_attribs=True)
class DeviceResults:
    """ """

    items: List[Device]
    pagination: Pagination

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "items": items,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Device.from_dict(items_item_data)

            items.append(items_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        device_results = cls(
            items=items,
            pagination=pagination,
        )

        return device_results
