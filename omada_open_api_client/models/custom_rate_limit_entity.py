from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomRateLimitEntity")


@_attrs_define
class CustomRateLimitEntity:
    """Custom configuration rate limit.

    Attributes:
        down_limit_enable (bool): Whether to enable downlink speed limit.
        up_limit_enable (bool): Whether to enable uplink speed limit.
        down_limit (Union[Unset, int]): Downlink speed limit in Kbps.Value of limit is from 0 to 10485760 Kbps.
        up_limit (Union[Unset, int]): Uplink speed limit in Kbps.Value of limit is from 0 to 10485760 Kbps.
    """

    down_limit_enable: bool
    up_limit_enable: bool
    down_limit: Union[Unset, int] = UNSET
    up_limit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        down_limit_enable = self.down_limit_enable
        up_limit_enable = self.up_limit_enable
        down_limit = self.down_limit
        up_limit = self.up_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downLimitEnable": down_limit_enable,
                "upLimitEnable": up_limit_enable,
            }
        )
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        down_limit_enable = d.pop("downLimitEnable")

        up_limit_enable = d.pop("upLimitEnable")

        down_limit = d.pop("downLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        custom_rate_limit_entity = cls(
            down_limit_enable=down_limit_enable,
            up_limit_enable=up_limit_enable,
            down_limit=down_limit,
            up_limit=up_limit,
        )

        custom_rate_limit_entity.additional_properties = d
        return custom_rate_limit_entity

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
