from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_lan_port_ipv_6_config_vo import OsgLanPortIpv6ConfigVO


T = TypeVar("T", bound="GatewayLanStatusEntity")


@_attrs_define
class GatewayLanStatusEntity:
    """
    Attributes:
        vlan (Union[Unset, int]): vlan
        lan_name (Union[Unset, str]): Lan name
        ip (Union[Unset, str]): Ip
        rx (Union[Unset, int]): Lan rx
        tx (Union[Unset, int]): Lan tx
        client_num (Union[Unset, int]): Lan client num
        lan_port_ipv_6_config (Union[Unset, OsgLanPortIpv6ConfigVO]): Lan ipv6 config
    """

    vlan: Union[Unset, int] = UNSET
    lan_name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    rx: Union[Unset, int] = UNSET
    tx: Union[Unset, int] = UNSET
    client_num: Union[Unset, int] = UNSET
    lan_port_ipv_6_config: Union[Unset, "OsgLanPortIpv6ConfigVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vlan = self.vlan
        lan_name = self.lan_name
        ip = self.ip
        rx = self.rx
        tx = self.tx
        client_num = self.client_num
        lan_port_ipv_6_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lan_port_ipv_6_config, Unset):
            lan_port_ipv_6_config = self.lan_port_ipv_6_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if lan_name is not UNSET:
            field_dict["lanName"] = lan_name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if lan_port_ipv_6_config is not UNSET:
            field_dict["lanPortIpv6Config"] = lan_port_ipv_6_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.osg_lan_port_ipv_6_config_vo import OsgLanPortIpv6ConfigVO

        d = src_dict.copy()
        vlan = d.pop("vlan", UNSET)

        lan_name = d.pop("lanName", UNSET)

        ip = d.pop("ip", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        client_num = d.pop("clientNum", UNSET)

        _lan_port_ipv_6_config = d.pop("lanPortIpv6Config", UNSET)
        lan_port_ipv_6_config: Union[Unset, OsgLanPortIpv6ConfigVO]
        if isinstance(_lan_port_ipv_6_config, Unset):
            lan_port_ipv_6_config = UNSET
        else:
            lan_port_ipv_6_config = OsgLanPortIpv6ConfigVO.from_dict(_lan_port_ipv_6_config)

        gateway_lan_status_entity = cls(
            vlan=vlan,
            lan_name=lan_name,
            ip=ip,
            rx=rx,
            tx=tx,
            client_num=client_num,
            lan_port_ipv_6_config=lan_port_ipv_6_config,
        )

        gateway_lan_status_entity.additional_properties = d
        return gateway_lan_status_entity

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
