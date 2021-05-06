from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attributes")


@attr.s(auto_attribs=True)
class Attributes:
    """ """

    os: Union[Unset, str] = UNSET
    ips: Union[Unset, List[None]] = UNSET
    fqdn: Union[Unset, List[None]] = UNSET
    groups: Union[Unset, List[None]] = UNSET
    hostname: Union[Unset, None] = UNSET
    os_category: Union[Unset, str] = UNSET
    recent_users: Union[Unset, List[None]] = UNSET
    mac_addresses: Union[Unset, List[None]] = UNSET
    mac_manufacturers: Union[Unset, List[None]] = UNSET
    distinguished_name: Union[Unset, None] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        os = self.os
        ips: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.ips, Unset):
            ips = []
            for ips_item_data in self.ips:
                ips_item = None

                ips.append(ips_item)

        fqdn: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.fqdn, Unset):
            fqdn = []
            for fqdn_item_data in self.fqdn:
                fqdn_item = None

                fqdn.append(fqdn_item)

        groups: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = None

                groups.append(groups_item)

        hostname = None

        os_category = self.os_category
        recent_users: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.recent_users, Unset):
            recent_users = []
            for recent_users_item_data in self.recent_users:
                recent_users_item = None

                recent_users.append(recent_users_item)

        mac_addresses: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.mac_addresses, Unset):
            mac_addresses = []
            for mac_addresses_item_data in self.mac_addresses:
                mac_addresses_item = None

                mac_addresses.append(mac_addresses_item)

        mac_manufacturers: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.mac_manufacturers, Unset):
            mac_manufacturers = []
            for mac_manufacturers_item_data in self.mac_manufacturers:
                mac_manufacturers_item = None

                mac_manufacturers.append(mac_manufacturers_item)

        distinguished_name = None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if os is not UNSET:
            field_dict["os"] = os
        if ips is not UNSET:
            field_dict["ips"] = ips
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if groups is not UNSET:
            field_dict["groups"] = groups
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if os_category is not UNSET:
            field_dict["os_category"] = os_category
        if recent_users is not UNSET:
            field_dict["recent_users"] = recent_users
        if mac_addresses is not UNSET:
            field_dict["mac_addresses"] = mac_addresses
        if mac_manufacturers is not UNSET:
            field_dict["mac_manufacturers"] = mac_manufacturers
        if distinguished_name is not UNSET:
            field_dict["distinguished_name"] = distinguished_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        os = d.pop("os", UNSET)

        ips = []
        _ips = d.pop("ips", UNSET)
        for ips_item_data in _ips or []:
            ips_item = None

            ips.append(ips_item)

        fqdn = []
        _fqdn = d.pop("fqdn", UNSET)
        for fqdn_item_data in _fqdn or []:
            fqdn_item = None

            fqdn.append(fqdn_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = None

            groups.append(groups_item)

        hostname = None

        os_category = d.pop("os_category", UNSET)

        recent_users = []
        _recent_users = d.pop("recent_users", UNSET)
        for recent_users_item_data in _recent_users or []:
            recent_users_item = None

            recent_users.append(recent_users_item)

        mac_addresses = []
        _mac_addresses = d.pop("mac_addresses", UNSET)
        for mac_addresses_item_data in _mac_addresses or []:
            mac_addresses_item = None

            mac_addresses.append(mac_addresses_item)

        mac_manufacturers = []
        _mac_manufacturers = d.pop("mac_manufacturers", UNSET)
        for mac_manufacturers_item_data in _mac_manufacturers or []:
            mac_manufacturers_item = None

            mac_manufacturers.append(mac_manufacturers_item)

        distinguished_name = None

        attributes = cls(
            os=os,
            ips=ips,
            fqdn=fqdn,
            groups=groups,
            hostname=hostname,
            os_category=os_category,
            recent_users=recent_users,
            mac_addresses=mac_addresses,
            mac_manufacturers=mac_manufacturers,
            distinguished_name=distinguished_name,
        )

        return attributes
