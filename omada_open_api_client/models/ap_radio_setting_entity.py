from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APRadioSettingEntity")


@_attrs_define
class APRadioSettingEntity:
    """radio setting 6g

    Attributes:
        radio_enable (Union[Unset, bool]): enable radio setting
        channel_width (Union[Unset, str]): RADIO_20 = 2; RADIO_40 = 3; RADIO_40_20 = 4（corresponding 2G Auto）; RADIO_80
            = 5; RADIO_80_40_20 = 6（corresponding 5G Auto）; RADIO_160= 7; RADIO_160_80_40_20 = 8; RADIO_240 = 9; RADIO_320 =
            10
        channel (Union[Unset, str]): channel
        tx_power (Union[Unset, int]): tx power
        tx_power_level (Union[Unset, int]): 0: Low; 1: Medium; 2: High; 3: Custom; 4: Auto;
        channel_limit_enable (Union[Unset, bool]): enable channel limit(site level)
        freq (Union[Unset, int]): frequency
        wireless_mode (Union[Unset, int]):
    """

    radio_enable: Union[Unset, bool] = UNSET
    channel_width: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    tx_power: Union[Unset, int] = UNSET
    tx_power_level: Union[Unset, int] = UNSET
    channel_limit_enable: Union[Unset, bool] = UNSET
    freq: Union[Unset, int] = UNSET
    wireless_mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        radio_enable = self.radio_enable
        channel_width = self.channel_width
        channel = self.channel
        tx_power = self.tx_power
        tx_power_level = self.tx_power_level
        channel_limit_enable = self.channel_limit_enable
        freq = self.freq
        wireless_mode = self.wireless_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_enable is not UNSET:
            field_dict["radioEnable"] = radio_enable
        if channel_width is not UNSET:
            field_dict["channelWidth"] = channel_width
        if channel is not UNSET:
            field_dict["channel"] = channel
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if tx_power_level is not UNSET:
            field_dict["txPowerLevel"] = tx_power_level
        if channel_limit_enable is not UNSET:
            field_dict["channelLimitEnable"] = channel_limit_enable
        if freq is not UNSET:
            field_dict["freq"] = freq
        if wireless_mode is not UNSET:
            field_dict["wirelessMode"] = wireless_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        radio_enable = d.pop("radioEnable", UNSET)

        channel_width = d.pop("channelWidth", UNSET)

        channel = d.pop("channel", UNSET)

        tx_power = d.pop("txPower", UNSET)

        tx_power_level = d.pop("txPowerLevel", UNSET)

        channel_limit_enable = d.pop("channelLimitEnable", UNSET)

        freq = d.pop("freq", UNSET)

        wireless_mode = d.pop("wirelessMode", UNSET)

        ap_radio_setting_entity = cls(
            radio_enable=radio_enable,
            channel_width=channel_width,
            channel=channel,
            tx_power=tx_power,
            tx_power_level=tx_power_level,
            channel_limit_enable=channel_limit_enable,
            freq=freq,
            wireless_mode=wireless_mode,
        )

        ap_radio_setting_entity.additional_properties = d
        return ap_radio_setting_entity

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
