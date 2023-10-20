from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Drop")


@_attrs_define
class Drop:
    """AP dropouts timing list

    Attributes:
        time (Union[Unset, int]): Sampling time second
        drop_times (Union[Unset, int]): Number of drop packets within one hour, such as 60 : 60%
        drop_rate (Union[Unset, float]): AP drop packet rate within one hour
    """

    time: Union[Unset, int] = UNSET
    drop_times: Union[Unset, int] = UNSET
    drop_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        drop_times = self.drop_times
        drop_rate = self.drop_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if drop_times is not UNSET:
            field_dict["dropTimes"] = drop_times
        if drop_rate is not UNSET:
            field_dict["dropRate"] = drop_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        drop_times = d.pop("dropTimes", UNSET)

        drop_rate = d.pop("dropRate", UNSET)

        drop = cls(
            time=time,
            drop_times=drop_times,
            drop_rate=drop_rate,
        )

        drop.additional_properties = d
        return drop

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
