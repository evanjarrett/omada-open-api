from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayPortSettingConfigEntity")


@_attrs_define
class GatewayPortSettingConfigEntity:
    """
    Attributes:
        link_speed (Union[Unset, int]): Port link speed
        duplex (Union[Unset, int]): Port duplex mode
        mirror_enable (Union[Unset, bool]): Port enabled mirror or not
        mirrored_ports (Union[Unset, List[int]]): Mirrored Ports Set
        mirror_mode (Union[Unset, int]): Port mirror mode
        pvid (Union[Unset, int]): Pvid(only for lan port.)
    """

    link_speed: Union[Unset, int] = UNSET
    duplex: Union[Unset, int] = UNSET
    mirror_enable: Union[Unset, bool] = UNSET
    mirrored_ports: Union[Unset, List[int]] = UNSET
    mirror_mode: Union[Unset, int] = UNSET
    pvid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_speed = self.link_speed
        duplex = self.duplex
        mirror_enable = self.mirror_enable
        mirrored_ports: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = self.mirrored_ports

        mirror_mode = self.mirror_mode
        pvid = self.pvid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if mirror_enable is not UNSET:
            field_dict["mirrorEnable"] = mirror_enable
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirror_mode is not UNSET:
            field_dict["mirrorMode"] = mirror_mode
        if pvid is not UNSET:
            field_dict["pvid"] = pvid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        mirror_enable = d.pop("mirrorEnable", UNSET)

        mirrored_ports = cast(List[int], d.pop("mirroredPorts", UNSET))

        mirror_mode = d.pop("mirrorMode", UNSET)

        pvid = d.pop("pvid", UNSET)

        gateway_port_setting_config_entity = cls(
            link_speed=link_speed,
            duplex=duplex,
            mirror_enable=mirror_enable,
            mirrored_ports=mirrored_ports,
            mirror_mode=mirror_mode,
            pvid=pvid,
        )

        gateway_port_setting_config_entity.additional_properties = d
        return gateway_port_setting_config_entity

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
