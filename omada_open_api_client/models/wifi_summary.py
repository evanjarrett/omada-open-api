from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WifiSummary")


@_attrs_define
class WifiSummary:
    """
    Attributes:
        connected_ap_num (Union[Unset, int]): The number of connected APs
        clients (Union[Unset, int]): The number of connected wireless clients
        channel_utilization (Union[Unset, int]): The average channel utilization of the 2.4GHz and 5GHz band for each AP
            in percentage. Null means no value.
        total_traffic (Union[Unset, float]): Total traffic measured in KB
    """

    connected_ap_num: Union[Unset, int] = UNSET
    clients: Union[Unset, int] = UNSET
    channel_utilization: Union[Unset, int] = UNSET
    total_traffic: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connected_ap_num = self.connected_ap_num
        clients = self.clients
        channel_utilization = self.channel_utilization
        total_traffic = self.total_traffic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_ap_num is not UNSET:
            field_dict["connectedApNum"] = connected_ap_num
        if clients is not UNSET:
            field_dict["clients"] = clients
        if channel_utilization is not UNSET:
            field_dict["channelUtilization"] = channel_utilization
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connected_ap_num = d.pop("connectedApNum", UNSET)

        clients = d.pop("clients", UNSET)

        channel_utilization = d.pop("channelUtilization", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        wifi_summary = cls(
            connected_ap_num=connected_ap_num,
            clients=clients,
            channel_utilization=channel_utilization,
            total_traffic=total_traffic,
        )

        wifi_summary.additional_properties = d
        return wifi_summary

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
