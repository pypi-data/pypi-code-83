from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="ClassificationBacktestForm")


@attr.s(auto_attribs=True)
class ClassificationBacktestForm:
    """  """

    file: Union[Unset, File] = UNSET
    options: Union[Unset, str] = "{}"
    start_date: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        options = self.options
        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if options is not UNSET:
            field_dict["options"] = options
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file: Union[Unset, File] = UNSET
        _file = d.pop("file", UNSET)
        if not isinstance(_file, Unset):
            file = File(payload=BytesIO(_file))

        options = d.pop("options", UNSET)

        start_date = d.pop("startDate", UNSET)

        classification_backtest_form = cls(
            file=file,
            options=options,
            start_date=start_date,
        )

        classification_backtest_form.additional_properties = d
        return classification_backtest_form

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
