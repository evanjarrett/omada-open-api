from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortPoe")


@_attrs_define
class PortPoe:
    """Device PoE Ports

    Attributes:
        port_id (Union[Unset, int]): switch port ID
        poe_supported (Union[Unset, bool]): switch port supported
        poe_enabled (Union[Unset, bool]): switch port enable
        poe_power (Union[Unset, int]): switch port power
        poe_percent (Union[Unset, int]): switch port percent
    """

    port_id: Union[Unset, int] = UNSET
    poe_supported: Union[Unset, bool] = UNSET
    poe_enabled: Union[Unset, bool] = UNSET
    poe_power: Union[Unset, int] = UNSET
    poe_percent: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port_id = self.port_id
        poe_supported = self.poe_supported
        poe_enabled = self.poe_enabled
        poe_power = self.poe_power
        poe_percent = self.poe_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if poe_supported is not UNSET:
            field_dict["poeSupported"] = poe_supported
        if poe_enabled is not UNSET:
            field_dict["poeEnabled"] = poe_enabled
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if poe_percent is not UNSET:
            field_dict["poePercent"] = poe_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        port_id = d.pop("portId", UNSET)

        poe_supported = d.pop("poeSupported", UNSET)

        poe_enabled = d.pop("poeEnabled", UNSET)

        poe_power = d.pop("poePower", UNSET)

        poe_percent = d.pop("poePercent", UNSET)

        port_poe = cls(
            port_id=port_id,
            poe_supported=poe_supported,
            poe_enabled=poe_enabled,
            poe_power=poe_power,
            poe_percent=poe_percent,
        )

        port_poe.additional_properties = d
        return port_poe

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
