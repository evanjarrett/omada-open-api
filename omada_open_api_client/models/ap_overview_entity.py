from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_wireless_uplink_entity import APWirelessUplinkEntity


T = TypeVar("T", bound="APOverviewEntity")


@_attrs_define
class APOverviewEntity:
    """
    Attributes:
        type (Union[Unset, str]): device type
        mac (Union[Unset, str]): device mac
        name (Union[Unset, str]): device name
        ip (Union[Unset, str]): device ip
        ipv_6_list (Union[Unset, List[str]]): device ipv6
        wlan_group_id (Union[Unset, str]): wlan group id
        wireless_uplink_info (Union[Unset, APWirelessUplinkEntity]): wireless uplink info
        model (Union[Unset, str]): device model
        firmware_version (Union[Unset, str]): device firmware version
        cpu_util (Union[Unset, int]): device cpu util(like 1 means 1% cpu util)
        memory_util (Union[Unset, int]): device memory util(like 50 means 50% memory util)
        uptime_long (Union[Unset, int]): device uptime(unit:second)
    """

    type: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    ipv_6_list: Union[Unset, List[str]] = UNSET
    wlan_group_id: Union[Unset, str] = UNSET
    wireless_uplink_info: Union[Unset, "APWirelessUplinkEntity"] = UNSET
    model: Union[Unset, str] = UNSET
    firmware_version: Union[Unset, str] = UNSET
    cpu_util: Union[Unset, int] = UNSET
    memory_util: Union[Unset, int] = UNSET
    uptime_long: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        mac = self.mac
        name = self.name
        ip = self.ip
        ipv_6_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        wlan_group_id = self.wlan_group_id
        wireless_uplink_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wireless_uplink_info, Unset):
            wireless_uplink_info = self.wireless_uplink_info.to_dict()

        model = self.model
        firmware_version = self.firmware_version
        cpu_util = self.cpu_util
        memory_util = self.memory_util
        uptime_long = self.uptime_long

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if wlan_group_id is not UNSET:
            field_dict["wlan group id"] = wlan_group_id
        if wireless_uplink_info is not UNSET:
            field_dict["wireless uplink info"] = wireless_uplink_info
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if memory_util is not UNSET:
            field_dict["memoryUtil"] = memory_util
        if uptime_long is not UNSET:
            field_dict["uptimeLong"] = uptime_long

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_wireless_uplink_entity import APWirelessUplinkEntity

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(List[str], d.pop("ipv6List", UNSET))

        wlan_group_id = d.pop("wlan group id", UNSET)

        _wireless_uplink_info = d.pop("wireless uplink info", UNSET)
        wireless_uplink_info: Union[Unset, APWirelessUplinkEntity]
        if isinstance(_wireless_uplink_info, Unset):
            wireless_uplink_info = UNSET
        else:
            wireless_uplink_info = APWirelessUplinkEntity.from_dict(_wireless_uplink_info)

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        memory_util = d.pop("memoryUtil", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        ap_overview_entity = cls(
            type=type,
            mac=mac,
            name=name,
            ip=ip,
            ipv_6_list=ipv_6_list,
            wlan_group_id=wlan_group_id,
            wireless_uplink_info=wireless_uplink_info,
            model=model,
            firmware_version=firmware_version,
            cpu_util=cpu_util,
            memory_util=memory_util,
            uptime_long=uptime_long,
        )

        ap_overview_entity.additional_properties = d
        return ap_overview_entity

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
