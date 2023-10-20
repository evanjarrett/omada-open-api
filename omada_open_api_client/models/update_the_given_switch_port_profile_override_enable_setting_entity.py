from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateTheGivenSwitchPortProfileOverrideEnableSettingEntity")


@_attrs_define
class UpdateTheGivenSwitchPortProfileOverrideEnableSettingEntity:
    """
    Attributes:
        profile_override_enable (bool): profileOverrideEnable
    """

    profile_override_enable: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_override_enable = self.profile_override_enable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileOverrideEnable": profile_override_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_override_enable = d.pop("profileOverrideEnable")

        update_the_given_switch_port_profile_override_enable_setting_entity = cls(
            profile_override_enable=profile_override_enable,
        )

        update_the_given_switch_port_profile_override_enable_setting_entity.additional_properties = d
        return update_the_given_switch_port_profile_override_enable_setting_entity

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
