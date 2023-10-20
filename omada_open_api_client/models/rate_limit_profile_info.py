from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitProfileInfo")


@_attrs_define
class RateLimitProfileInfo:
    """
    Attributes:
        name (str): Rate limit profile name.
        down_limit_enable (bool): Down limit enable.
        up_limit_enable (bool): Up limit enable.
        id (Union[Unset, str]): Rate limit profile id.
        site (Union[Unset, str]): site id
        down_limit (Union[Unset, int]): Down limit. Unit is Kbps, integer from 1 to 10485760.
        up_limit (Union[Unset, int]): Up limit. Unit is Kbps, integer from 1 to 10485760.
        is_default (Union[Unset, bool]): Whether it is default profile.
    """

    name: str
    down_limit_enable: bool
    up_limit_enable: bool
    id: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    down_limit: Union[Unset, int] = UNSET
    up_limit: Union[Unset, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        down_limit_enable = self.down_limit_enable
        up_limit_enable = self.up_limit_enable
        id = self.id
        site = self.site
        down_limit = self.down_limit
        up_limit = self.up_limit
        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "downLimitEnable": down_limit_enable,
                "upLimitEnable": up_limit_enable,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site is not UNSET:
            field_dict["site"] = site
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        down_limit_enable = d.pop("downLimitEnable")

        up_limit_enable = d.pop("upLimitEnable")

        id = d.pop("id", UNSET)

        site = d.pop("site", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        is_default = d.pop("isDefault", UNSET)

        rate_limit_profile_info = cls(
            name=name,
            down_limit_enable=down_limit_enable,
            up_limit_enable=up_limit_enable,
            id=id,
            site=site,
            down_limit=down_limit,
            up_limit=up_limit,
            is_default=is_default,
        )

        rate_limit_profile_info.additional_properties = d
        return rate_limit_profile_info

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
