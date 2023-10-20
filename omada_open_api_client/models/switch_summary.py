from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchSummary")


@_attrs_define
class SwitchSummary:
    """
    Attributes:
        clients (Union[Unset, int]): Number of wired clients
        port_utilization (Union[Unset, int]): Port occupancy rate (integer)
        connected_switch_num (Union[Unset, int]): Number of online switches
        total_traffic (Union[Unset, int]): Upstream and downstream traffic and the unit (Byte) of online switches
    """

    clients: Union[Unset, int] = UNSET
    port_utilization: Union[Unset, int] = UNSET
    connected_switch_num: Union[Unset, int] = UNSET
    total_traffic: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clients = self.clients
        port_utilization = self.port_utilization
        connected_switch_num = self.connected_switch_num
        total_traffic = self.total_traffic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients
        if port_utilization is not UNSET:
            field_dict["portUtilization"] = port_utilization
        if connected_switch_num is not UNSET:
            field_dict["connectedSwitchNum"] = connected_switch_num
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clients = d.pop("clients", UNSET)

        port_utilization = d.pop("portUtilization", UNSET)

        connected_switch_num = d.pop("connectedSwitchNum", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        switch_summary = cls(
            clients=clients,
            port_utilization=port_utilization,
            connected_switch_num=connected_switch_num,
            total_traffic=total_traffic,
        )

        switch_summary.additional_properties = d
        return switch_summary

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
