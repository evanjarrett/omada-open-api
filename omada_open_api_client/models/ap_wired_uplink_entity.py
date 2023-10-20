from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APWiredUplinkEntity")


@_attrs_define
class APWiredUplinkEntity:
    """wired uplink info

    Attributes:
        uplink_mac (Union[Unset, str]): uplink device mac address
        type (Union[Unset, str]): uplink device type
        name (Union[Unset, str]): uplink device name
        rate (Union[Unset, str]): Negotiation rate, LAN(connected):10,100,1000,2500,10000, LAN(disconnected):0,
            Unit:Mbps
        duplex (Union[Unset, int]): 0: LAN disconnected, 1: half, 2: full
        up_bytes (Union[Unset, int]): Unit:Byte
        down_bytes (Union[Unset, int]): Unit:Byte
        up_packets (Union[Unset, int]):
        down_packets (Union[Unset, int]):
        activity (Union[Unset, int]): (change of(downBytes+upBytes))/time, Unit:B/s
    """

    uplink_mac: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rate: Union[Unset, str] = UNSET
    duplex: Union[Unset, int] = UNSET
    up_bytes: Union[Unset, int] = UNSET
    down_bytes: Union[Unset, int] = UNSET
    up_packets: Union[Unset, int] = UNSET
    down_packets: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uplink_mac = self.uplink_mac
        type = self.type
        name = self.name
        rate = self.rate
        duplex = self.duplex
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
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
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

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        duplex = d.pop("duplex", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_packets = d.pop("upPackets", UNSET)

        down_packets = d.pop("downPackets", UNSET)

        activity = d.pop("activity", UNSET)

        ap_wired_uplink_entity = cls(
            uplink_mac=uplink_mac,
            type=type,
            name=name,
            rate=rate,
            duplex=duplex,
            up_bytes=up_bytes,
            down_bytes=down_bytes,
            up_packets=up_packets,
            down_packets=down_packets,
            activity=activity,
        )

        ap_wired_uplink_entity.additional_properties = d
        return ap_wired_uplink_entity

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
