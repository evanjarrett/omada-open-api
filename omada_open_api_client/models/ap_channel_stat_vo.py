from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApChannelStatVO")


@_attrs_define
class ApChannelStatVO:
    """
    Attributes:
        channel (Union[Unset, int]):
        ap_num (Union[Unset, int]):
        client_num (Union[Unset, int]):
        channel_utilization (Union[Unset, float]):
    """

    channel: Union[Unset, int] = UNSET
    ap_num: Union[Unset, int] = UNSET
    client_num: Union[Unset, int] = UNSET
    channel_utilization: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel = self.channel
        ap_num = self.ap_num
        client_num = self.client_num
        channel_utilization = self.channel_utilization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ap_num is not UNSET:
            field_dict["apNum"] = ap_num
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if channel_utilization is not UNSET:
            field_dict["channelUtilization"] = channel_utilization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel = d.pop("channel", UNSET)

        ap_num = d.pop("apNum", UNSET)

        client_num = d.pop("clientNum", UNSET)

        channel_utilization = d.pop("channelUtilization", UNSET)

        ap_channel_stat_vo = cls(
            channel=channel,
            ap_num=ap_num,
            client_num=client_num,
            channel_utilization=channel_utilization,
        )

        ap_channel_stat_vo.additional_properties = d
        return ap_channel_stat_vo

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
