from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_channel_stat_vo import ApChannelStatVO


T = TypeVar("T", bound="ApChannelsStatVO")


@_attrs_define
class ApChannelsStatVO:
    """
    Attributes:
        channels2g (Union[Unset, List['ApChannelStatVO']]):
        channels5g (Union[Unset, List['ApChannelStatVO']]):
        channels6g (Union[Unset, List['ApChannelStatVO']]):
    """

    channels2g: Union[Unset, List["ApChannelStatVO"]] = UNSET
    channels5g: Union[Unset, List["ApChannelStatVO"]] = UNSET
    channels6g: Union[Unset, List["ApChannelStatVO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channels2g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channels2g, Unset):
            channels2g = []
            for channels2g_item_data in self.channels2g:
                channels2g_item = channels2g_item_data.to_dict()

                channels2g.append(channels2g_item)

        channels5g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channels5g, Unset):
            channels5g = []
            for channels5g_item_data in self.channels5g:
                channels5g_item = channels5g_item_data.to_dict()

                channels5g.append(channels5g_item)

        channels6g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channels6g, Unset):
            channels6g = []
            for channels6g_item_data in self.channels6g:
                channels6g_item = channels6g_item_data.to_dict()

                channels6g.append(channels6g_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels2g is not UNSET:
            field_dict["channels2g"] = channels2g
        if channels5g is not UNSET:
            field_dict["channels5g"] = channels5g
        if channels6g is not UNSET:
            field_dict["channels6g"] = channels6g

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_channel_stat_vo import ApChannelStatVO

        d = src_dict.copy()
        channels2g = []
        _channels2g = d.pop("channels2g", UNSET)
        for channels2g_item_data in _channels2g or []:
            channels2g_item = ApChannelStatVO.from_dict(channels2g_item_data)

            channels2g.append(channels2g_item)

        channels5g = []
        _channels5g = d.pop("channels5g", UNSET)
        for channels5g_item_data in _channels5g or []:
            channels5g_item = ApChannelStatVO.from_dict(channels5g_item_data)

            channels5g.append(channels5g_item)

        channels6g = []
        _channels6g = d.pop("channels6g", UNSET)
        for channels6g_item_data in _channels6g or []:
            channels6g_item = ApChannelStatVO.from_dict(channels6g_item_data)

            channels6g.append(channels6g_item)

        ap_channels_stat_vo = cls(
            channels2g=channels2g,
            channels5g=channels5g,
            channels6g=channels6g,
        )

        ap_channels_stat_vo.additional_properties = d
        return ap_channels_stat_vo

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
