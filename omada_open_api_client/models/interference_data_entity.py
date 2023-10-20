from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterferenceDataEntity")


@_attrs_define
class InterferenceDataEntity:
    """Interference data, the data refer to the interference intensity and the times of interferences, and they are used to
    create histograms.

        Attributes:
            str_ (Union[Unset, List[int]]): Interference strength, range [-91, -89, -87, …., -33, -31, -29] (up to 32
                strength levels), for example: -91 means the range is -92-90.
            cnt (Union[Unset, List[int]]): interference counts, range [0, 200]
    """

    str_: Union[Unset, List[int]] = UNSET
    cnt: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        str_: Union[Unset, List[int]] = UNSET
        if not isinstance(self.str_, Unset):
            str_ = self.str_

        cnt: Union[Unset, List[int]] = UNSET
        if not isinstance(self.cnt, Unset):
            cnt = self.cnt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if str_ is not UNSET:
            field_dict["str"] = str_
        if cnt is not UNSET:
            field_dict["cnt"] = cnt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        str_ = cast(List[int], d.pop("str", UNSET))

        cnt = cast(List[int], d.pop("cnt", UNSET))

        interference_data_entity = cls(
            str_=str_,
            cnt=cnt,
        )

        interference_data_entity.additional_properties = d
        return interference_data_entity

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
