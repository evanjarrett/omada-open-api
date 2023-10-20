from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandCtrlEntity")


@_attrs_define
class BandCtrlEntity:
    """bandCtrl

    Attributes:
        egress_enable (bool): egress enable status
        ingress_enable (bool): ingress enable status
        egress_limit (Union[Unset, int]): egressLimit
        egress_unit (Union[Unset, int]): 1 means 1Kps and 2 means Mbps
        ingress_limit (Union[Unset, int]): ingressLimit
        ingress_unit (Union[Unset, int]): 1 means 1Kps and 2 means Mbps
    """

    egress_enable: bool
    ingress_enable: bool
    egress_limit: Union[Unset, int] = UNSET
    egress_unit: Union[Unset, int] = UNSET
    ingress_limit: Union[Unset, int] = UNSET
    ingress_unit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        egress_enable = self.egress_enable
        ingress_enable = self.ingress_enable
        egress_limit = self.egress_limit
        egress_unit = self.egress_unit
        ingress_limit = self.ingress_limit
        ingress_unit = self.ingress_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "egressEnable": egress_enable,
                "ingressEnable": ingress_enable,
            }
        )
        if egress_limit is not UNSET:
            field_dict["egressLimit"] = egress_limit
        if egress_unit is not UNSET:
            field_dict["egressUnit"] = egress_unit
        if ingress_limit is not UNSET:
            field_dict["ingressLimit"] = ingress_limit
        if ingress_unit is not UNSET:
            field_dict["ingressUnit"] = ingress_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        egress_enable = d.pop("egressEnable")

        ingress_enable = d.pop("ingressEnable")

        egress_limit = d.pop("egressLimit", UNSET)

        egress_unit = d.pop("egressUnit", UNSET)

        ingress_limit = d.pop("ingressLimit", UNSET)

        ingress_unit = d.pop("ingressUnit", UNSET)

        band_ctrl_entity = cls(
            egress_enable=egress_enable,
            ingress_enable=ingress_enable,
            egress_limit=egress_limit,
            egress_unit=egress_unit,
            ingress_limit=ingress_limit,
            ingress_unit=ingress_unit,
        )

        band_ctrl_entity.additional_properties = d
        return band_ctrl_entity

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
