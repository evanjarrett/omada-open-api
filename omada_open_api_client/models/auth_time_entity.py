from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTimeEntity")


@_attrs_define
class AuthTimeEntity:
    """Authentication timeout time. Display when enabled, otherwise no display.

    Attributes:
        auth_timeout (int): Validity period * 0: Custom, 1: 30 Minutes, 2: 1 Hour, 3: 2 Hours, 4: 4 Hours, 5: 8 Hours,
            6: 1 Day, 7: 7 Days integer.
        custom_timeout (Union[Unset, int]): Custom timeout,  1 ~ 1,000,000 min,  * 1 ~ 10,000 hour,  * 1 ~ 1,000 day.
        custom_timeout_unit (Union[Unset, int]): Custom timeout unit: 1: min, 2: hour, 3: day.
    """

    auth_timeout: int
    custom_timeout: Union[Unset, int] = UNSET
    custom_timeout_unit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_timeout = self.auth_timeout
        custom_timeout = self.custom_timeout
        custom_timeout_unit = self.custom_timeout_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authTimeout": auth_timeout,
            }
        )
        if custom_timeout is not UNSET:
            field_dict["customTimeout"] = custom_timeout
        if custom_timeout_unit is not UNSET:
            field_dict["customTimeoutUnit"] = custom_timeout_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_timeout = d.pop("authTimeout")

        custom_timeout = d.pop("customTimeout", UNSET)

        custom_timeout_unit = d.pop("customTimeoutUnit", UNSET)

        auth_time_entity = cls(
            auth_timeout=auth_timeout,
            custom_timeout=custom_timeout,
            custom_timeout_unit=custom_timeout_unit,
        )

        auth_time_entity.additional_properties = d
        return auth_time_entity

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
