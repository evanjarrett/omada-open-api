from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APRadioChannelEntity")


@_attrs_define
class APRadioChannelEntity:
    """radio channel 6g

    Attributes:
        actual_channel (Union[Unset, str]):
        max_tx_rate (Union[Unset, int]):
        tx_power (Union[Unset, int]):
        region (Union[Unset, int]):
        band_width (Union[Unset, str]):
        rd_mode (Union[Unset, str]):
        tx_util (Union[Unset, int]):
        rx_util (Union[Unset, int]):
        inter_util (Union[Unset, int]):
        busy_util (Union[Unset, int]): MTK model(busyUtil = txUtil + rxUtil + interUtil)
    """

    actual_channel: Union[Unset, str] = UNSET
    max_tx_rate: Union[Unset, int] = UNSET
    tx_power: Union[Unset, int] = UNSET
    region: Union[Unset, int] = UNSET
    band_width: Union[Unset, str] = UNSET
    rd_mode: Union[Unset, str] = UNSET
    tx_util: Union[Unset, int] = UNSET
    rx_util: Union[Unset, int] = UNSET
    inter_util: Union[Unset, int] = UNSET
    busy_util: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actual_channel = self.actual_channel
        max_tx_rate = self.max_tx_rate
        tx_power = self.tx_power
        region = self.region
        band_width = self.band_width
        rd_mode = self.rd_mode
        tx_util = self.tx_util
        rx_util = self.rx_util
        inter_util = self.inter_util
        busy_util = self.busy_util

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_channel is not UNSET:
            field_dict["actualChannel"] = actual_channel
        if max_tx_rate is not UNSET:
            field_dict["maxTxRate"] = max_tx_rate
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if region is not UNSET:
            field_dict["region"] = region
        if band_width is not UNSET:
            field_dict["bandWidth"] = band_width
        if rd_mode is not UNSET:
            field_dict["rdMode"] = rd_mode
        if tx_util is not UNSET:
            field_dict["txUtil"] = tx_util
        if rx_util is not UNSET:
            field_dict["rxUtil"] = rx_util
        if inter_util is not UNSET:
            field_dict["interUtil"] = inter_util
        if busy_util is not UNSET:
            field_dict["busyUtil"] = busy_util

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actual_channel = d.pop("actualChannel", UNSET)

        max_tx_rate = d.pop("maxTxRate", UNSET)

        tx_power = d.pop("txPower", UNSET)

        region = d.pop("region", UNSET)

        band_width = d.pop("bandWidth", UNSET)

        rd_mode = d.pop("rdMode", UNSET)

        tx_util = d.pop("txUtil", UNSET)

        rx_util = d.pop("rxUtil", UNSET)

        inter_util = d.pop("interUtil", UNSET)

        busy_util = d.pop("busyUtil", UNSET)

        ap_radio_channel_entity = cls(
            actual_channel=actual_channel,
            max_tx_rate=max_tx_rate,
            tx_power=tx_power,
            region=region,
            band_width=band_width,
            rd_mode=rd_mode,
            tx_util=tx_util,
            rx_util=rx_util,
            inter_util=inter_util,
            busy_util=busy_util,
        )

        ap_radio_channel_entity.additional_properties = d
        return ap_radio_channel_entity

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
