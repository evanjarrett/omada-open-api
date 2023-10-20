from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BatchUpdateGivenSwitchPortsProfileOverrideEnableSettingEntity")


@_attrs_define
class BatchUpdateGivenSwitchPortsProfileOverrideEnableSettingEntity:
    """
    Attributes:
        port_list (List[int]): portList
        profile_override_enable (bool): profileOverrideEnable
    """

    port_list: List[int]
    profile_override_enable: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port_list = self.port_list

        profile_override_enable = self.profile_override_enable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portList": port_list,
                "profileOverrideEnable": profile_override_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        port_list = cast(List[int], d.pop("portList"))

        profile_override_enable = d.pop("profileOverrideEnable")

        batch_update_given_switch_ports_profile_override_enable_setting_entity = cls(
            port_list=port_list,
            profile_override_enable=profile_override_enable,
        )

        batch_update_given_switch_ports_profile_override_enable_setting_entity.additional_properties = d
        return batch_update_given_switch_ports_profile_override_enable_setting_entity

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
