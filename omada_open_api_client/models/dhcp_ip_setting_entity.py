from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpIpSettingEntity")


@_attrs_define
class DhcpIpSettingEntity:
    """dhcp ip setting

    Attributes:
        fallback (Union[Unset, bool]): enable/disable fallback(if false, other params is not required)
        fallback_ip (Union[Unset, str]): fallback IP address
        fallback_mask (Union[Unset, str]): fallback IP mask
        fallback_gate (Union[Unset, str]): fallback gateway IP address
        use_fixed_addr (Union[Unset, bool]): enable reserved address(Gateway required)
        net_id (Union[Unset, str]): network id
        dhcp_ip (Union[Unset, str]): reserved ip address
    """

    fallback: Union[Unset, bool] = UNSET
    fallback_ip: Union[Unset, str] = UNSET
    fallback_mask: Union[Unset, str] = UNSET
    fallback_gate: Union[Unset, str] = UNSET
    use_fixed_addr: Union[Unset, bool] = UNSET
    net_id: Union[Unset, str] = UNSET
    dhcp_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fallback = self.fallback
        fallback_ip = self.fallback_ip
        fallback_mask = self.fallback_mask
        fallback_gate = self.fallback_gate
        use_fixed_addr = self.use_fixed_addr
        net_id = self.net_id
        dhcp_ip = self.dhcp_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if fallback_ip is not UNSET:
            field_dict["fallbackIp"] = fallback_ip
        if fallback_mask is not UNSET:
            field_dict["fallbackMask"] = fallback_mask
        if fallback_gate is not UNSET:
            field_dict["fallbackGate"] = fallback_gate
        if use_fixed_addr is not UNSET:
            field_dict["useFixedAddr"] = use_fixed_addr
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if dhcp_ip is not UNSET:
            field_dict["dhcpIp"] = dhcp_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fallback = d.pop("fallback", UNSET)

        fallback_ip = d.pop("fallbackIp", UNSET)

        fallback_mask = d.pop("fallbackMask", UNSET)

        fallback_gate = d.pop("fallbackGate", UNSET)

        use_fixed_addr = d.pop("useFixedAddr", UNSET)

        net_id = d.pop("netId", UNSET)

        dhcp_ip = d.pop("dhcpIp", UNSET)

        dhcp_ip_setting_entity = cls(
            fallback=fallback,
            fallback_ip=fallback_ip,
            fallback_mask=fallback_mask,
            fallback_gate=fallback_gate,
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            dhcp_ip=dhcp_ip,
        )

        dhcp_ip_setting_entity.additional_properties = d
        return dhcp_ip_setting_entity

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
