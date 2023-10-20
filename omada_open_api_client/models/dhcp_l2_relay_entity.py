from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpL2RelayEntity")


@_attrs_define
class DhcpL2RelayEntity:
    """dhcpL2RelaySettings

    Attributes:
        enable (Union[Unset, bool]): enable
        format_ (Union[Unset, int]): 0 means normal and 1 means private
    """

    enable: Union[Unset, bool] = UNSET
    format_: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        format_ = d.pop("format", UNSET)

        dhcp_l2_relay_entity = cls(
            enable=enable,
            format_=format_,
        )

        dhcp_l2_relay_entity.additional_properties = d
        return dhcp_l2_relay_entity

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
