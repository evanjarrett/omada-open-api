from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgWanPortIpv6ConfigVO")


@_attrs_define
class OsgWanPortIpv6ConfigVO:
    """Wan ipv6 config

    Attributes:
        enable (Union[Unset, int]):
        proto (Union[Unset, str]):
        addr (Union[Unset, str]):
        gateway (Union[Unset, str]):
        pri_dns (Union[Unset, str]):
        snd_dns (Union[Unset, str]):
        internet_state (Union[Unset, int]):
    """

    enable: Union[Unset, int] = UNSET
    proto: Union[Unset, str] = UNSET
    addr: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    pri_dns: Union[Unset, str] = UNSET
    snd_dns: Union[Unset, str] = UNSET
    internet_state: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        proto = self.proto
        addr = self.addr
        gateway = self.gateway
        pri_dns = self.pri_dns
        snd_dns = self.snd_dns
        internet_state = self.internet_state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if proto is not UNSET:
            field_dict["proto"] = proto
        if addr is not UNSET:
            field_dict["addr"] = addr
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        proto = d.pop("proto", UNSET)

        addr = d.pop("addr", UNSET)

        gateway = d.pop("gateway", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        internet_state = d.pop("internetState", UNSET)

        osg_wan_port_ipv_6_config_vo = cls(
            enable=enable,
            proto=proto,
            addr=addr,
            gateway=gateway,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            internet_state=internet_state,
        )

        osg_wan_port_ipv_6_config_vo.additional_properties = d
        return osg_wan_port_ipv_6_config_vo

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
