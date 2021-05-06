from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """ """

    created: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    last_login: Union[Unset, str] = UNSET
    login_count: Union[Unset, int] = UNSET
    mfa_enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    picture: Union[Unset, str] = UNSET
    roles: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created
        email = self.email
        last_login = self.last_login
        login_count = self.login_count
        mfa_enabled = self.mfa_enabled
        name = self.name
        nickname = self.nickname
        picture = self.picture
        roles: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if email is not UNSET:
            field_dict["email"] = email
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if login_count is not UNSET:
            field_dict["login_count"] = login_count
        if mfa_enabled is not UNSET:
            field_dict["mfa_enabled"] = mfa_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if picture is not UNSET:
            field_dict["picture"] = picture
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created", UNSET)

        email = d.pop("email", UNSET)

        last_login = d.pop("last_login", UNSET)

        login_count = d.pop("login_count", UNSET)

        mfa_enabled = d.pop("mfa_enabled", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        picture = d.pop("picture", UNSET)

        roles = cast(List[str], d.pop("roles", UNSET))

        user = cls(
            created=created,
            email=email,
            last_login=last_login,
            login_count=login_count,
            mfa_enabled=mfa_enabled,
            name=name,
            nickname=nickname,
            picture=picture,
            roles=roles,
        )

        user.additional_properties = d
        return user

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
