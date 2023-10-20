from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_limit_setting_vo import ChannelLimitSettingVO


T = TypeVar("T", bound="SiteSettingchannelLimit")


@_attrs_define
class SiteSettingchannelLimit:
    """
    Attributes:
        channel_limit (Union[Unset, ChannelLimitSettingVO]):
    """

    channel_limit: Union[Unset, "ChannelLimitSettingVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.channel_limit, Unset):
            channel_limit = self.channel_limit.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_limit is not UNSET:
            field_dict["channelLimit"] = channel_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel_limit_setting_vo import ChannelLimitSettingVO

        d = src_dict.copy()
        _channel_limit = d.pop("channelLimit", UNSET)
        channel_limit: Union[Unset, ChannelLimitSettingVO]
        if isinstance(_channel_limit, Unset):
            channel_limit = UNSET
        else:
            channel_limit = ChannelLimitSettingVO.from_dict(_channel_limit)

        site_settingchannel_limit = cls(
            channel_limit=channel_limit,
        )

        site_settingchannel_limit.additional_properties = d
        return site_settingchannel_limit

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
