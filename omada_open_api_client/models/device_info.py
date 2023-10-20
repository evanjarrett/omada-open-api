from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInfo")


@_attrs_define
class DeviceInfo:
    """
    Attributes:
        mac (Union[Unset, str]): Device mac
        name (Union[Unset, str]): Device name
        type (Union[Unset, str]): Device type
        model (Union[Unset, str]): Device model name
        ip (Union[Unset, str]): Device ip
        ipv6 (Union[Unset, List[str]]): Device ipv6 list
        uptime (Union[Unset, str]): Device uptime
        status (Union[Unset, int]): Device status. 0:Disconnected; 1:Connected; 2:Pending; 3:Heartbeat Missed;
            4:Isolated
        last_seen (Union[Unset, int]): Device lastSeen
        cpu_util (Union[Unset, int]): Device cpuUtil
        mem_util (Union[Unset, int]): Device memUtil
        sn (Union[Unset, str]): Device sn
        license_status (Union[Unset, int]): Device license status(Only for cloud base). 0:unActive; 1:Unbind; 2:Expired;
            3:active
    """

    mac: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    ipv6: Union[Unset, List[str]] = UNSET
    uptime: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    last_seen: Union[Unset, int] = UNSET
    cpu_util: Union[Unset, int] = UNSET
    mem_util: Union[Unset, int] = UNSET
    sn: Union[Unset, str] = UNSET
    license_status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mac = self.mac
        name = self.name
        type = self.type
        model = self.model
        ip = self.ip
        ipv6: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6

        uptime = self.uptime
        status = self.status
        last_seen = self.last_seen
        cpu_util = self.cpu_util
        mem_util = self.mem_util
        sn = self.sn
        license_status = self.license_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if model is not UNSET:
            field_dict["model"] = model
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if status is not UNSET:
            field_dict["status"] = status
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if sn is not UNSET:
            field_dict["sn"] = sn
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        ip = d.pop("ip", UNSET)

        ipv6 = cast(List[str], d.pop("ipv6", UNSET))

        uptime = d.pop("uptime", UNSET)

        status = d.pop("status", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        sn = d.pop("sn", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        device_info = cls(
            mac=mac,
            name=name,
            type=type,
            model=model,
            ip=ip,
            ipv6=ipv6,
            uptime=uptime,
            status=status,
            last_seen=last_seen,
            cpu_util=cpu_util,
            mem_util=mem_util,
            sn=sn,
            license_status=license_status,
        )

        device_info.additional_properties = d
        return device_info

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
