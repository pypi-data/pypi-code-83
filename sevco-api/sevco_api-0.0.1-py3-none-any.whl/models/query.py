from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_rule import QueryRule
from ..types import UNSET, Unset

T = TypeVar("T", bound="Query")


@attr.s(auto_attribs=True)
class Query:
    """ """

    combinator: Union[Unset, str] = UNSET
    rules: Union[Unset, List[QueryRule]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        combinator = self.combinator
        rules: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combinator is not UNSET:
            field_dict["combinator"] = combinator
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        combinator = d.pop("combinator", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = QueryRule.from_dict(rules_item_data)

            rules.append(rules_item)

        query = cls(
            combinator=combinator,
            rules=rules,
        )

        query.additional_properties = d
        return query

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
