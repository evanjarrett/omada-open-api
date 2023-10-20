from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgLanPortIpv6ConfigVO")


@_attrs_define
class OsgLanPortIpv6ConfigVO:
    """Lan ipv6 config

    Attributes:
        addr (Union[Unset, str]):
        gw (Union[Unset, str]):
        pri_dns (Union[Unset, str]):
        snd_dns (Union[Unset, str]):
    """

    addr: Union[Unset, str] = UNSET
    gw: Union[Unset, str] = UNSET
    pri_dns: Union[Unset, str] = UNSET
    snd_dns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addr = self.addr
        gw = self.gw
        pri_dns = self.pri_dns
        snd_dns = self.snd_dns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if gw is not UNSET:
            field_dict["gw"] = gw
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        addr = d.pop("addr", UNSET)

        gw = d.pop("gw", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        osg_lan_port_ipv_6_config_vo = cls(
            addr=addr,
            gw=gw,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        osg_lan_port_ipv_6_config_vo.additional_properties = d
        return osg_lan_port_ipv_6_config_vo

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
