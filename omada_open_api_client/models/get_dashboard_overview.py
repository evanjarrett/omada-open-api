from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDashboardOverview")


@_attrs_define
class GetDashboardOverview:
    """
    Attributes:
        total_gateway_num (Union[Unset, int]): The total number of gateways
        connected_gateway_num (Union[Unset, int]): The number of connected gateways
        disconnected_gateway_num (Union[Unset, int]): The number of disconnected gateways
        net_capacity (Union[Unset, int]): Network Capacity measured in Mbps. Null means no value.
        net_usage (Union[Unset, float]): The current link usage rate under the Gateway node (percent conversion has been
            performed, such as 98.1)
        total_switch_num (Union[Unset, int]): Total number of switches
        connected_switch_num (Union[Unset, int]): Number of switches in connected state
        disconnected_switch_num (Union[Unset, int]): Number of switches in disconnected state
        total_ports (Union[Unset, int]): Total number of ports
        available_ports (Union[Unset, int]): Number of valid ports
        power_consumption (Union[Unset, float]): Power consumption (unit: W)
        total_ap_num (Union[Unset, int]): Total number of APs
        connected_ap_num (Union[Unset, int]): Number of APs in connected state
        isolated_ap_num (Union[Unset, int]): Number of APs in isolated state
        disconnected_ap_num (Union[Unset, int]): Number of APs in disconnected state
        total_client_num (Union[Unset, int]): Total number of clients
        wired_client_num (Union[Unset, int]): Number of wired clients
        wireless_client_num (Union[Unset, int]): Number of wireless clients
        guest_num (Union[Unset, int]): Number of wireless guest clients
    """

    total_gateway_num: Union[Unset, int] = UNSET
    connected_gateway_num: Union[Unset, int] = UNSET
    disconnected_gateway_num: Union[Unset, int] = UNSET
    net_capacity: Union[Unset, int] = UNSET
    net_usage: Union[Unset, float] = UNSET
    total_switch_num: Union[Unset, int] = UNSET
    connected_switch_num: Union[Unset, int] = UNSET
    disconnected_switch_num: Union[Unset, int] = UNSET
    total_ports: Union[Unset, int] = UNSET
    available_ports: Union[Unset, int] = UNSET
    power_consumption: Union[Unset, float] = UNSET
    total_ap_num: Union[Unset, int] = UNSET
    connected_ap_num: Union[Unset, int] = UNSET
    isolated_ap_num: Union[Unset, int] = UNSET
    disconnected_ap_num: Union[Unset, int] = UNSET
    total_client_num: Union[Unset, int] = UNSET
    wired_client_num: Union[Unset, int] = UNSET
    wireless_client_num: Union[Unset, int] = UNSET
    guest_num: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_gateway_num = self.total_gateway_num
        connected_gateway_num = self.connected_gateway_num
        disconnected_gateway_num = self.disconnected_gateway_num
        net_capacity = self.net_capacity
        net_usage = self.net_usage
        total_switch_num = self.total_switch_num
        connected_switch_num = self.connected_switch_num
        disconnected_switch_num = self.disconnected_switch_num
        total_ports = self.total_ports
        available_ports = self.available_ports
        power_consumption = self.power_consumption
        total_ap_num = self.total_ap_num
        connected_ap_num = self.connected_ap_num
        isolated_ap_num = self.isolated_ap_num
        disconnected_ap_num = self.disconnected_ap_num
        total_client_num = self.total_client_num
        wired_client_num = self.wired_client_num
        wireless_client_num = self.wireless_client_num
        guest_num = self.guest_num

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_gateway_num is not UNSET:
            field_dict["totalGatewayNum"] = total_gateway_num
        if connected_gateway_num is not UNSET:
            field_dict["connectedGatewayNum"] = connected_gateway_num
        if disconnected_gateway_num is not UNSET:
            field_dict["disconnectedGatewayNum"] = disconnected_gateway_num
        if net_capacity is not UNSET:
            field_dict["netCapacity"] = net_capacity
        if net_usage is not UNSET:
            field_dict["netUsage"] = net_usage
        if total_switch_num is not UNSET:
            field_dict["totalSwitchNum"] = total_switch_num
        if connected_switch_num is not UNSET:
            field_dict["connectedSwitchNum"] = connected_switch_num
        if disconnected_switch_num is not UNSET:
            field_dict["disconnectedSwitchNum"] = disconnected_switch_num
        if total_ports is not UNSET:
            field_dict["totalPorts"] = total_ports
        if available_ports is not UNSET:
            field_dict["availablePorts"] = available_ports
        if power_consumption is not UNSET:
            field_dict["powerConsumption"] = power_consumption
        if total_ap_num is not UNSET:
            field_dict["totalApNum"] = total_ap_num
        if connected_ap_num is not UNSET:
            field_dict["connectedApNum"] = connected_ap_num
        if isolated_ap_num is not UNSET:
            field_dict["isolatedApNum"] = isolated_ap_num
        if disconnected_ap_num is not UNSET:
            field_dict["disconnectedApNum"] = disconnected_ap_num
        if total_client_num is not UNSET:
            field_dict["totalClientNum"] = total_client_num
        if wired_client_num is not UNSET:
            field_dict["wiredClientNum"] = wired_client_num
        if wireless_client_num is not UNSET:
            field_dict["wirelessClientNum"] = wireless_client_num
        if guest_num is not UNSET:
            field_dict["guestNum"] = guest_num

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_gateway_num = d.pop("totalGatewayNum", UNSET)

        connected_gateway_num = d.pop("connectedGatewayNum", UNSET)

        disconnected_gateway_num = d.pop("disconnectedGatewayNum", UNSET)

        net_capacity = d.pop("netCapacity", UNSET)

        net_usage = d.pop("netUsage", UNSET)

        total_switch_num = d.pop("totalSwitchNum", UNSET)

        connected_switch_num = d.pop("connectedSwitchNum", UNSET)

        disconnected_switch_num = d.pop("disconnectedSwitchNum", UNSET)

        total_ports = d.pop("totalPorts", UNSET)

        available_ports = d.pop("availablePorts", UNSET)

        power_consumption = d.pop("powerConsumption", UNSET)

        total_ap_num = d.pop("totalApNum", UNSET)

        connected_ap_num = d.pop("connectedApNum", UNSET)

        isolated_ap_num = d.pop("isolatedApNum", UNSET)

        disconnected_ap_num = d.pop("disconnectedApNum", UNSET)

        total_client_num = d.pop("totalClientNum", UNSET)

        wired_client_num = d.pop("wiredClientNum", UNSET)

        wireless_client_num = d.pop("wirelessClientNum", UNSET)

        guest_num = d.pop("guestNum", UNSET)

        get_dashboard_overview = cls(
            total_gateway_num=total_gateway_num,
            connected_gateway_num=connected_gateway_num,
            disconnected_gateway_num=disconnected_gateway_num,
            net_capacity=net_capacity,
            net_usage=net_usage,
            total_switch_num=total_switch_num,
            connected_switch_num=connected_switch_num,
            disconnected_switch_num=disconnected_switch_num,
            total_ports=total_ports,
            available_ports=available_ports,
            power_consumption=power_consumption,
            total_ap_num=total_ap_num,
            connected_ap_num=connected_ap_num,
            isolated_ap_num=isolated_ap_num,
            disconnected_ap_num=disconnected_ap_num,
            total_client_num=total_client_num,
            wired_client_num=wired_client_num,
            wireless_client_num=wireless_client_num,
            guest_num=guest_num,
        )

        get_dashboard_overview.additional_properties = d
        return get_dashboard_overview

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
