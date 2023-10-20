from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTrafficActivity")


@_attrs_define
class DeviceTrafficActivity:
    """Wireless network total traffic timing list Wired network total traffic timing list,

    Attributes:
        time (Union[Unset, int]): The timestamp of this data sample
        tx_data (Union[Unset, float]): Uplink traffic in MB
        dx_data (Union[Unset, float]): Downlink traffic in MB
    """

    time: Union[Unset, int] = UNSET
    tx_data: Union[Unset, float] = UNSET
    dx_data: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        tx_data = self.tx_data
        dx_data = self.dx_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if tx_data is not UNSET:
            field_dict["txData"] = tx_data
        if dx_data is not UNSET:
            field_dict["dxData"] = dx_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        tx_data = d.pop("txData", UNSET)

        dx_data = d.pop("dxData", UNSET)

        device_traffic_activity = cls(
            time=time,
            tx_data=tx_data,
            dx_data=dx_data,
        )

        device_traffic_activity.additional_properties = d
        return device_traffic_activity

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
