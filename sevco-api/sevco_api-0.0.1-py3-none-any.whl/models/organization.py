from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """ """

    created: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mfa_enabled: Union[Unset, bool] = UNSET
    org_name: Union[Unset, str] = UNSET
    org_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created
        id = self.id
        mfa_enabled = self.mfa_enabled
        org_name = self.org_name
        org_slug = self.org_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if mfa_enabled is not UNSET:
            field_dict["mfa_enabled"] = mfa_enabled
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        mfa_enabled = d.pop("mfa_enabled", UNSET)

        org_name = d.pop("org_name", UNSET)

        org_slug = d.pop("org_slug", UNSET)

        organization = cls(
            created=created,
            id=id,
            mfa_enabled=mfa_enabled,
            org_name=org_name,
            org_slug=org_slug,
        )

        organization.additional_properties = d
        return organization

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
