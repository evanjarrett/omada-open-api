from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Retry")


@_attrs_define
class Retry:
    """AP retries timing list

    Attributes:
        time (Union[Unset, int]): Sampling time second
        retry_times (Union[Unset, int]): Number of new contracts within one hour, such as 60 : 60%
        retry_rate (Union[Unset, float]): AP re-contracting rate within one hour
    """

    time: Union[Unset, int] = UNSET
    retry_times: Union[Unset, int] = UNSET
    retry_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        retry_times = self.retry_times
        retry_rate = self.retry_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if retry_times is not UNSET:
            field_dict["retryTimes"] = retry_times
        if retry_rate is not UNSET:
            field_dict["retryRate"] = retry_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        retry_times = d.pop("retryTimes", UNSET)

        retry_rate = d.pop("retryRate", UNSET)

        retry = cls(
            time=time,
            retry_times=retry_times,
            retry_rate=retry_rate,
        )

        retry.additional_properties = d
        return retry

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
