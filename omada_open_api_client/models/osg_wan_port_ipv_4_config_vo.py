from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgWanPortIpv4ConfigVO")


@_attrs_define
class OsgWanPortIpv4ConfigVO:
    """Wan ipv4 config

    Attributes:
        ip (Union[Unset, str]):
        ip2 (Union[Unset, str]):
        gateway (Union[Unset, str]):
        gateway2 (Union[Unset, str]):
        pri_dns (Union[Unset, str]):
        snd_dns (Union[Unset, str]):
        pri_dns_2 (Union[Unset, str]):
        snd_dns_2 (Union[Unset, str]):
    """

    ip: Union[Unset, str] = UNSET
    ip2: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    gateway2: Union[Unset, str] = UNSET
    pri_dns: Union[Unset, str] = UNSET
    snd_dns: Union[Unset, str] = UNSET
    pri_dns_2: Union[Unset, str] = UNSET
    snd_dns_2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip
        ip2 = self.ip2
        gateway = self.gateway
        gateway2 = self.gateway2
        pri_dns = self.pri_dns
        snd_dns = self.snd_dns
        pri_dns_2 = self.pri_dns_2
        snd_dns_2 = self.snd_dns_2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ip2 is not UNSET:
            field_dict["ip2"] = ip2
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gateway2 is not UNSET:
            field_dict["gateway2"] = gateway2
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if pri_dns_2 is not UNSET:
            field_dict["priDns2"] = pri_dns_2
        if snd_dns_2 is not UNSET:
            field_dict["sndDns2"] = snd_dns_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip", UNSET)

        ip2 = d.pop("ip2", UNSET)

        gateway = d.pop("gateway", UNSET)

        gateway2 = d.pop("gateway2", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        pri_dns_2 = d.pop("priDns2", UNSET)

        snd_dns_2 = d.pop("sndDns2", UNSET)

        osg_wan_port_ipv_4_config_vo = cls(
            ip=ip,
            ip2=ip2,
            gateway=gateway,
            gateway2=gateway2,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            pri_dns_2=pri_dns_2,
            snd_dns_2=snd_dns_2,
        )

        osg_wan_port_ipv_4_config_vo.additional_properties = d
        return osg_wan_port_ipv_4_config_vo

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
