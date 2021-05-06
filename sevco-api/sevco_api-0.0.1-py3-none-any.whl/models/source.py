from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Source")


@attr.s(auto_attribs=True)
class Source:
    """ """

    config_id: str
    id: str
    last_observed_timestamp: str
    last_activity_timestamp: str
    source: str
    version: str

    def to_dict(self) -> Dict[str, Any]:
        config_id = self.config_id
        id = self.id
        last_observed_timestamp = self.last_observed_timestamp
        last_activity_timestamp = self.last_activity_timestamp
        source = self.source
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "config_id": config_id,
                "id": id,
                "last_observed_timestamp": last_observed_timestamp,
                "last_activity_timestamp": last_activity_timestamp,
                "source": source,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_id = d.pop("config_id")

        id = d.pop("id")

        last_observed_timestamp = d.pop("last_observed_timestamp")

        last_activity_timestamp = d.pop("last_activity_timestamp")

        source = d.pop("source")

        version = d.pop("version")

        source = cls(
            config_id=config_id,
            id=id,
            last_observed_timestamp=last_observed_timestamp,
            last_activity_timestamp=last_activity_timestamp,
            source=source,
            version=version,
        )

        return source
