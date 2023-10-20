from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_vo import DeviceLocationDetailVO


T = TypeVar("T", bound="APGeneralConfigEntity")


@_attrs_define
class APGeneralConfigEntity:
    """
    Attributes:
        name (Union[Unset, str]): device name(Parameter [name] should be 1 ~ 128 characters)
        led_setting (Union[Unset, int]): led setting(Parameter [ledSetting] should be 0 or 1 or 2)
        tag_ids (Union[Unset, List[str]]): tag ids
        location (Union[Unset, DeviceLocationDetailVO]): device location
    """

    name: Union[Unset, str] = UNSET
    led_setting: Union[Unset, int] = UNSET
    tag_ids: Union[Unset, List[str]] = UNSET
    location: Union[Unset, "DeviceLocationDetailVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        led_setting = self.led_setting
        tag_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_location_detail_vo import DeviceLocationDetailVO

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        tag_ids = cast(List[str], d.pop("tagIds", UNSET))

        _location = d.pop("location", UNSET)
        location: Union[Unset, DeviceLocationDetailVO]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        ap_general_config_entity = cls(
            name=name,
            led_setting=led_setting,
            tag_ids=tag_ids,
            location=location,
        )

        ap_general_config_entity.additional_properties = d
        return ap_general_config_entity

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
