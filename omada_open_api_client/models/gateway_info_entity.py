from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_port_config_entity import GatewayPortConfigEntity


T = TypeVar("T", bound="GatewayInfoEntity")


@_attrs_define
class GatewayInfoEntity:
    """
    Attributes:
        mac (Union[Unset, str]): Gateway mac address
        show_model (Union[Unset, str]): Gateway model description
        firmware_version (Union[Unset, str]): Gateway software version
        ip (Union[Unset, str]): Gateway ipv4
        uptime (Union[Unset, str]): Gateway uptime
        temp (Union[Unset, int]): Gateway temperature
        cpu_util (Union[Unset, int]): Gateway cpu utilization rate
        mem_util (Union[Unset, int]): Gateway memory utilization rate
        ipv_6_list (Union[Unset, List[str]]): ipv6 address List
        last_seen (Union[Unset, int]): last seen time
        port_configs (Union[Unset, List['GatewayPortConfigEntity']]): Gateway port configs
    """

    mac: Union[Unset, str] = UNSET
    show_model: Union[Unset, str] = UNSET
    firmware_version: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    uptime: Union[Unset, str] = UNSET
    temp: Union[Unset, int] = UNSET
    cpu_util: Union[Unset, int] = UNSET
    mem_util: Union[Unset, int] = UNSET
    ipv_6_list: Union[Unset, List[str]] = UNSET
    last_seen: Union[Unset, int] = UNSET
    port_configs: Union[Unset, List["GatewayPortConfigEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mac = self.mac
        show_model = self.show_model
        firmware_version = self.firmware_version
        ip = self.ip
        uptime = self.uptime
        temp = self.temp
        cpu_util = self.cpu_util
        mem_util = self.mem_util
        ipv_6_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        last_seen = self.last_seen
        port_configs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.port_configs, Unset):
            port_configs = []
            for port_configs_item_data in self.port_configs:
                port_configs_item = port_configs_item_data.to_dict()

                port_configs.append(port_configs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if temp is not UNSET:
            field_dict["temp"] = temp
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if port_configs is not UNSET:
            field_dict["portConfigs"] = port_configs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_port_config_entity import GatewayPortConfigEntity

        d = src_dict.copy()
        mac = d.pop("mac", UNSET)

        show_model = d.pop("showModel", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        ip = d.pop("ip", UNSET)

        uptime = d.pop("uptime", UNSET)

        temp = d.pop("temp", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        ipv_6_list = cast(List[str], d.pop("ipv6List", UNSET))

        last_seen = d.pop("lastSeen", UNSET)

        port_configs = []
        _port_configs = d.pop("portConfigs", UNSET)
        for port_configs_item_data in _port_configs or []:
            port_configs_item = GatewayPortConfigEntity.from_dict(port_configs_item_data)

            port_configs.append(port_configs_item)

        gateway_info_entity = cls(
            mac=mac,
            show_model=show_model,
            firmware_version=firmware_version,
            ip=ip,
            uptime=uptime,
            temp=temp,
            cpu_util=cpu_util,
            mem_util=mem_util,
            ipv_6_list=ipv_6_list,
            last_seen=last_seen,
            port_configs=port_configs,
        )

        gateway_info_entity.additional_properties = d
        return gateway_info_entity

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
