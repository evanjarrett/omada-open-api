from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StormCtrlEntity")


@_attrs_define
class StormCtrlEntity:
    """stormCtrl

    Attributes:
        unknown_unicast_enable (bool): unknown-Unicast enable status
        multicast_enable (bool): multicast enable status
        broadcast_enable (bool): broadcast enable status
        action (int): action, 0 means drop and 1 means shutdown, default drop
        unknown_unicast (Union[Unset, int]): unknown-Unicast
        multicast (Union[Unset, int]): multicast
        broadcast (Union[Unset, int]): broadcast
        recover_time (Union[Unset, int]): recoverTime, default 3600
    """

    unknown_unicast_enable: bool
    multicast_enable: bool
    broadcast_enable: bool
    action: int
    unknown_unicast: Union[Unset, int] = UNSET
    multicast: Union[Unset, int] = UNSET
    broadcast: Union[Unset, int] = UNSET
    recover_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unknown_unicast_enable = self.unknown_unicast_enable
        multicast_enable = self.multicast_enable
        broadcast_enable = self.broadcast_enable
        action = self.action
        unknown_unicast = self.unknown_unicast
        multicast = self.multicast
        broadcast = self.broadcast
        recover_time = self.recover_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unknownUnicastEnable": unknown_unicast_enable,
                "multicastEnable": multicast_enable,
                "broadcastEnable": broadcast_enable,
                "action": action,
            }
        )
        if unknown_unicast is not UNSET:
            field_dict["unknownUnicast"] = unknown_unicast
        if multicast is not UNSET:
            field_dict["multicast"] = multicast
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if recover_time is not UNSET:
            field_dict["recoverTime"] = recover_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unknown_unicast_enable = d.pop("unknownUnicastEnable")

        multicast_enable = d.pop("multicastEnable")

        broadcast_enable = d.pop("broadcastEnable")

        action = d.pop("action")

        unknown_unicast = d.pop("unknownUnicast", UNSET)

        multicast = d.pop("multicast", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        recover_time = d.pop("recoverTime", UNSET)

        storm_ctrl_entity = cls(
            unknown_unicast_enable=unknown_unicast_enable,
            multicast_enable=multicast_enable,
            broadcast_enable=broadcast_enable,
            action=action,
            unknown_unicast=unknown_unicast,
            multicast=multicast,
            broadcast=broadcast,
            recover_time=recover_time,
        )

        storm_ctrl_entity.additional_properties = d
        return storm_ctrl_entity

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
