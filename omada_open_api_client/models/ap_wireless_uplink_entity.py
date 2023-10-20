from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APWirelessUplinkEntity")


@_attrs_define
class APWirelessUplinkEntity:
    """wireless uplink info

    Attributes:
        uplink_mac (Union[Unset, str]): uplink ap mac
        name (Union[Unset, str]):
        channel (Union[Unset, int]):
        rssi (Union[Unset, int]):
        snr (Union[Unset, int]): signal-noise ratio
        tx_rate (Union[Unset, str]):
        rx_rate_int (Union[Unset, int]): unit:Mbps
        rx_rate (Union[Unset, str]):
        up_bytes (Union[Unset, int]):
        down_bytes (Union[Unset, int]):
        up_packets (Union[Unset, int]):
        down_packets (Union[Unset, int]):
        activity (Union[Unset, int]): (change of(downBytes+upBytes))/time
    """

    uplink_mac: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    channel: Union[Unset, int] = UNSET
    rssi: Union[Unset, int] = UNSET
    snr: Union[Unset, int] = UNSET
    tx_rate: Union[Unset, str] = UNSET
    rx_rate_int: Union[Unset, int] = UNSET
    rx_rate: Union[Unset, str] = UNSET
    up_bytes: Union[Unset, int] = UNSET
    down_bytes: Union[Unset, int] = UNSET
    up_packets: Union[Unset, int] = UNSET
    down_packets: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uplink_mac = self.uplink_mac
        name = self.name
        channel = self.channel
        rssi = self.rssi
        snr = self.snr
        tx_rate = self.tx_rate
        rx_rate_int = self.rx_rate_int
        rx_rate = self.rx_rate
        up_bytes = self.up_bytes
        down_bytes = self.down_bytes
        up_packets = self.up_packets
        down_packets = self.down_packets
        activity = self.activity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uplink_mac is not UNSET:
            field_dict["uplinkMac"] = uplink_mac
        if name is not UNSET:
            field_dict["name"] = name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate_int is not UNSET:
            field_dict["rxRateInt"] = rx_rate_int
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_packets is not UNSET:
            field_dict["upPackets"] = up_packets
        if down_packets is not UNSET:
            field_dict["downPackets"] = down_packets
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uplink_mac = d.pop("uplinkMac", UNSET)

        name = d.pop("name", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate_int = d.pop("rxRateInt", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_packets = d.pop("upPackets", UNSET)

        down_packets = d.pop("downPackets", UNSET)

        activity = d.pop("activity", UNSET)

        ap_wireless_uplink_entity = cls(
            uplink_mac=uplink_mac,
            name=name,
            channel=channel,
            rssi=rssi,
            snr=snr,
            tx_rate=tx_rate,
            rx_rate_int=rx_rate_int,
            rx_rate=rx_rate,
            up_bytes=up_bytes,
            down_bytes=down_bytes,
            up_packets=up_packets,
            down_packets=down_packets,
            activity=activity,
        )

        ap_wireless_uplink_entity.additional_properties = d
        return ap_wireless_uplink_entity

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
