from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.configured_source_auth import ConfiguredSourceAuth
from ..models.configured_source_connect import ConfiguredSourceConnect
from ..models.configured_source_settings import ConfiguredSourceSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfiguredSource")


@attr.s(auto_attribs=True)
class ConfiguredSource:
    """ """

    auth: ConfiguredSourceAuth
    connect: ConfiguredSourceConnect
    created_timestamp: str
    enabled: bool
    id: str
    last_updated_timestamp: str
    org_id: str
    settings: ConfiguredSourceSettings
    source_id: str
    plugin_id: Union[Unset, str] = UNSET
    runner_id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    categories: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        auth = self.auth.to_dict()

        connect = self.connect.to_dict()

        created_timestamp = self.created_timestamp
        enabled = self.enabled
        id = self.id
        last_updated_timestamp = self.last_updated_timestamp
        org_id = self.org_id
        settings = self.settings.to_dict()

        source_id = self.source_id
        plugin_id = self.plugin_id
        runner_id = self.runner_id
        display_name = self.display_name
        source_type = self.source_type
        categories: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "auth": auth,
                "connect": connect,
                "created_timestamp": created_timestamp,
                "enabled": enabled,
                "id": id,
                "last_updated_timestamp": last_updated_timestamp,
                "org_id": org_id,
                "settings": settings,
                "source_id": source_id,
            }
        )
        if plugin_id is not UNSET:
            field_dict["plugin_id"] = plugin_id
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth = ConfiguredSourceAuth.from_dict(d.pop("auth"))

        connect = ConfiguredSourceConnect.from_dict(d.pop("connect"))

        created_timestamp = d.pop("created_timestamp")

        enabled = d.pop("enabled")

        id = d.pop("id")

        last_updated_timestamp = d.pop("last_updated_timestamp")

        org_id = d.pop("org_id")

        settings = ConfiguredSourceSettings.from_dict(d.pop("settings"))

        source_id = d.pop("source_id")

        plugin_id = d.pop("plugin_id", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        source_type = d.pop("source_type", UNSET)

        categories = cast(List[str], d.pop("categories", UNSET))

        configured_source = cls(
            auth=auth,
            connect=connect,
            created_timestamp=created_timestamp,
            enabled=enabled,
            id=id,
            last_updated_timestamp=last_updated_timestamp,
            org_id=org_id,
            settings=settings,
            source_id=source_id,
            plugin_id=plugin_id,
            runner_id=runner_id,
            display_name=display_name,
            source_type=source_type,
            categories=categories,
        )

        return configured_source
