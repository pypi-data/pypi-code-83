from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attributes import Attributes
from ..models.source import Source
from ..types import UNSET, Unset

T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """ """

    id: str
    last_observed_timestamp: str
    first_observed_timestamp: str
    org_id: str
    version: str
    attributes: Attributes
    sources: List[Source]
    last_activity_timestamp: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        last_observed_timestamp = self.last_observed_timestamp
        first_observed_timestamp = self.first_observed_timestamp
        org_id = self.org_id
        version = self.version
        attributes = self.attributes.to_dict()

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()

            sources.append(sources_item)

        last_activity_timestamp = self.last_activity_timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "last_observed_timestamp": last_observed_timestamp,
                "first_observed_timestamp": first_observed_timestamp,
                "org_id": org_id,
                "version": version,
                "attributes": attributes,
                "sources": sources,
            }
        )
        if last_activity_timestamp is not UNSET:
            field_dict["last_activity_timestamp"] = last_activity_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        last_observed_timestamp = d.pop("last_observed_timestamp")

        first_observed_timestamp = d.pop("first_observed_timestamp")

        org_id = d.pop("org_id")

        version = d.pop("version")

        attributes = Attributes.from_dict(d.pop("attributes"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = Source.from_dict(sources_item_data)

            sources.append(sources_item)

        last_activity_timestamp = d.pop("last_activity_timestamp", UNSET)

        device = cls(
            id=id,
            last_observed_timestamp=last_observed_timestamp,
            first_observed_timestamp=first_observed_timestamp,
            org_id=org_id,
            version=version,
            attributes=attributes,
            sources=sources,
            last_activity_timestamp=last_activity_timestamp,
        )

        return device
