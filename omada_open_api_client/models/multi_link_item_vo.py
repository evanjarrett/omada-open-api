from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiLinkItemVO")


@_attrs_define
class MultiLinkItemVO:
    """
    Attributes:
        radio_id (Union[Unset, int]):
        wifi_mode (Union[Unset, int]):
        channel (Union[Unset, int]):
        rx_rate (Union[Unset, int]):
        tx_rate (Union[Unset, int]):
        power_save (Union[Unset, bool]):
        rssi (Union[Unset, int]):
        snr (Union[Unset, int]):
        signal_level (Union[Unset, int]):
        signal_rank (Union[Unset, int]):
        up_packet (Union[Unset, int]):
        down_packet (Union[Unset, int]):
        traffic_down (Union[Unset, int]):
        traffic_up (Union[Unset, int]):
        activity (Union[Unset, int]):
        signal_level_and_rank (Union[Unset, int]):
    """

    radio_id: Union[Unset, int] = UNSET
    wifi_mode: Union[Unset, int] = UNSET
    channel: Union[Unset, int] = UNSET
    rx_rate: Union[Unset, int] = UNSET
    tx_rate: Union[Unset, int] = UNSET
    power_save: Union[Unset, bool] = UNSET
    rssi: Union[Unset, int] = UNSET
    snr: Union[Unset, int] = UNSET
    signal_level: Union[Unset, int] = UNSET
    signal_rank: Union[Unset, int] = UNSET
    up_packet: Union[Unset, int] = UNSET
    down_packet: Union[Unset, int] = UNSET
    traffic_down: Union[Unset, int] = UNSET
    traffic_up: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    signal_level_and_rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        radio_id = self.radio_id
        wifi_mode = self.wifi_mode
        channel = self.channel
        rx_rate = self.rx_rate
        tx_rate = self.tx_rate
        power_save = self.power_save
        rssi = self.rssi
        snr = self.snr
        signal_level = self.signal_level
        signal_rank = self.signal_rank
        up_packet = self.up_packet
        down_packet = self.down_packet
        traffic_down = self.traffic_down
        traffic_up = self.traffic_up
        activity = self.activity
        signal_level_and_rank = self.signal_level_and_rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if wifi_mode is not UNSET:
            field_dict["wifiMode"] = wifi_mode
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if power_save is not UNSET:
            field_dict["powerSave"] = power_save
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if signal_rank is not UNSET:
            field_dict["signalRank"] = signal_rank
        if up_packet is not UNSET:
            field_dict["upPacket"] = up_packet
        if down_packet is not UNSET:
            field_dict["downPacket"] = down_packet
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if activity is not UNSET:
            field_dict["activity"] = activity
        if signal_level_and_rank is not UNSET:
            field_dict["signalLevelAndRank"] = signal_level_and_rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        radio_id = d.pop("radioId", UNSET)

        wifi_mode = d.pop("wifiMode", UNSET)

        channel = d.pop("channel", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        power_save = d.pop("powerSave", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        signal_rank = d.pop("signalRank", UNSET)

        up_packet = d.pop("upPacket", UNSET)

        down_packet = d.pop("downPacket", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        activity = d.pop("activity", UNSET)

        signal_level_and_rank = d.pop("signalLevelAndRank", UNSET)

        multi_link_item_vo = cls(
            radio_id=radio_id,
            wifi_mode=wifi_mode,
            channel=channel,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            power_save=power_save,
            rssi=rssi,
            snr=snr,
            signal_level=signal_level,
            signal_rank=signal_rank,
            up_packet=up_packet,
            down_packet=down_packet,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            activity=activity,
            signal_level_and_rank=signal_level_and_rank,
        )

        multi_link_item_vo.additional_properties = d
        return multi_link_item_vo

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
