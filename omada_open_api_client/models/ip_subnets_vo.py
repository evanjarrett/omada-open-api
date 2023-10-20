from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSubnetsVO")


@_attrs_define
class IPSubnetsVO:
    """Custom networks of the VPN.

    Attributes:
        ip (Union[Unset, str]):
        mask (Union[Unset, int]):
    """

    ip: Union[Unset, str] = UNSET
    mask: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip
        mask = self.mask

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip", UNSET)

        mask = d.pop("mask", UNSET)

        ip_subnets_vo = cls(
            ip=ip,
            mask=mask,
        )

        ip_subnets_vo.additional_properties = d
        return ip_subnets_vo

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
