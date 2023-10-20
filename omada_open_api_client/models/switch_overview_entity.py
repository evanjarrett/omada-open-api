from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_info_entity import PortInfoEntity


T = TypeVar("T", bound="SwitchOverviewEntity")


@_attrs_define
class SwitchOverviewEntity:
    """
    Attributes:
        mac (Union[Unset, str]): switch mac address
        ip (Union[Unset, str]): switch ip address
        ipv_6_list (Union[Unset, List[str]]): switch ipv6 List
        model (Union[Unset, str]): model
        firmware_version (Union[Unset, str]): firmware Version e.g:2.5.0 Build 20190118 Rel. 64821
        version (Union[Unset, str]): firmware Version e.g:2.5.0
        hw_version (Union[Unset, str]): Hardware Version
        cpu_util (Union[Unset, int]): cpuUtil
        mem_util (Union[Unset, int]): memUtil
        uptime (Union[Unset, str]): uptime
        port_list (Union[Unset, List['PortInfoEntity']]): portList
    """

    mac: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    ipv_6_list: Union[Unset, List[str]] = UNSET
    model: Union[Unset, str] = UNSET
    firmware_version: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    hw_version: Union[Unset, str] = UNSET
    cpu_util: Union[Unset, int] = UNSET
    mem_util: Union[Unset, int] = UNSET
    uptime: Union[Unset, str] = UNSET
    port_list: Union[Unset, List["PortInfoEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mac = self.mac
        ip = self.ip
        ipv_6_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        model = self.model
        firmware_version = self.firmware_version
        version = self.version
        hw_version = self.hw_version
        cpu_util = self.cpu_util
        mem_util = self.mem_util
        uptime = self.uptime
        port_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()

                port_list.append(port_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if version is not UNSET:
            field_dict["version"] = version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.port_info_entity import PortInfoEntity

        d = src_dict.copy()
        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(List[str], d.pop("ipv6List", UNSET))

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        version = d.pop("version", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        uptime = d.pop("uptime", UNSET)

        port_list = []
        _port_list = d.pop("portList", UNSET)
        for port_list_item_data in _port_list or []:
            port_list_item = PortInfoEntity.from_dict(port_list_item_data)

            port_list.append(port_list_item)

        switch_overview_entity = cls(
            mac=mac,
            ip=ip,
            ipv_6_list=ipv_6_list,
            model=model,
            firmware_version=firmware_version,
            version=version,
            hw_version=hw_version,
            cpu_util=cpu_util,
            mem_util=mem_util,
            uptime=uptime,
            port_list=port_list,
        )

        switch_overview_entity.additional_properties = d
        return switch_overview_entity

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
