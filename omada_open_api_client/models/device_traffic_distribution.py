from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTrafficDistribution")


@_attrs_define
class DeviceTrafficDistribution:
    """Current Site Switch List

    Attributes:
        name (Union[Unset, str]): Device Name
        mac (Union[Unset, str]): Device MAC
        traffic (Union[Unset, float]): Device traffic measured in MB
        traffic_proportion (Union[Unset, float]): The proportion of AP traffic in percentage
    """

    name: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    traffic: Union[Unset, float] = UNSET
    traffic_proportion: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        mac = self.mac
        traffic = self.traffic
        traffic_proportion = self.traffic_proportion

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_proportion is not UNSET:
            field_dict["trafficProportion"] = traffic_proportion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_proportion = d.pop("trafficProportion", UNSET)

        device_traffic_distribution = cls(
            name=name,
            mac=mac,
            traffic=traffic,
            traffic_proportion=traffic_proportion,
        )

        device_traffic_distribution.additional_properties = d
        return device_traffic_distribution

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
