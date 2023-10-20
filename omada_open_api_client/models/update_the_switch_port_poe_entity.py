from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateTheSwitchPortPoeEntity")


@_attrs_define
class UpdateTheSwitchPortPoeEntity:
    """
    Attributes:
        poe_mode (int): poe mode, 1 means on(802.3at/af), 0 means off
    """

    poe_mode: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        poe_mode = self.poe_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "poeMode": poe_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        poe_mode = d.pop("poeMode")

        update_the_switch_port_poe_entity = cls(
            poe_mode=poe_mode,
        )

        update_the_switch_port_poe_entity.additional_properties = d
        return update_the_switch_port_poe_entity

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
