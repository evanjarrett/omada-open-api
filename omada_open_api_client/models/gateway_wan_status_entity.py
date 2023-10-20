from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_wan_port_ipv_4_config_vo import OsgWanPortIpv4ConfigVO
    from ..models.osg_wan_port_ipv_6_config_vo import OsgWanPortIpv6ConfigVO


T = TypeVar("T", bound="GatewayWanStatusEntity")


@_attrs_define
class GatewayWanStatusEntity:
    """
    Attributes:
        port (Union[Unset, int]): Port serial number
        name (Union[Unset, str]): Port name
        port_desc (Union[Unset, str]): Port description
        status (Union[Unset, int]): Port status, 0-disconnected; 1-connected;
        internet_state (Union[Unset, int]): Wan internet state, 0-disconnected; 1-connected;
        wan_port_ipv_6_config (Union[Unset, OsgWanPortIpv6ConfigVO]): Wan ipv6 config
        wan_port_ipv_4_config (Union[Unset, OsgWanPortIpv4ConfigVO]): Wan ipv4 config
        rx_rate (Union[Unset, int]): Port rx rate, Unit: KB/s;
        tx_rate (Union[Unset, int]): Port tx rate, Unit: KB/s;
        latency (Union[Unset, int]): Wan latency, when mode is wan and device is connected, Unit: ms
        loss (Union[Unset, float]): Wan packet loss rate, Unit : %
    """

    port: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    port_desc: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    internet_state: Union[Unset, int] = UNSET
    wan_port_ipv_6_config: Union[Unset, "OsgWanPortIpv6ConfigVO"] = UNSET
    wan_port_ipv_4_config: Union[Unset, "OsgWanPortIpv4ConfigVO"] = UNSET
    rx_rate: Union[Unset, int] = UNSET
    tx_rate: Union[Unset, int] = UNSET
    latency: Union[Unset, int] = UNSET
    loss: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port = self.port
        name = self.name
        port_desc = self.port_desc
        status = self.status
        internet_state = self.internet_state
        wan_port_ipv_6_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wan_port_ipv_6_config, Unset):
            wan_port_ipv_6_config = self.wan_port_ipv_6_config.to_dict()

        wan_port_ipv_4_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = self.wan_port_ipv_4_config.to_dict()

        rx_rate = self.rx_rate
        tx_rate = self.tx_rate
        latency = self.latency
        loss = self.loss

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if port_desc is not UNSET:
            field_dict["portDesc"] = port_desc
        if status is not UNSET:
            field_dict["status"] = status
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if wan_port_ipv_6_config is not UNSET:
            field_dict["wanPortIpv6Config"] = wan_port_ipv_6_config
        if wan_port_ipv_4_config is not UNSET:
            field_dict["wanPortIpv4Config"] = wan_port_ipv_4_config
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.osg_wan_port_ipv_4_config_vo import OsgWanPortIpv4ConfigVO
        from ..models.osg_wan_port_ipv_6_config_vo import OsgWanPortIpv6ConfigVO

        d = src_dict.copy()
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        port_desc = d.pop("portDesc", UNSET)

        status = d.pop("status", UNSET)

        internet_state = d.pop("internetState", UNSET)

        _wan_port_ipv_6_config = d.pop("wanPortIpv6Config", UNSET)
        wan_port_ipv_6_config: Union[Unset, OsgWanPortIpv6ConfigVO]
        if isinstance(_wan_port_ipv_6_config, Unset):
            wan_port_ipv_6_config = UNSET
        else:
            wan_port_ipv_6_config = OsgWanPortIpv6ConfigVO.from_dict(_wan_port_ipv_6_config)

        _wan_port_ipv_4_config = d.pop("wanPortIpv4Config", UNSET)
        wan_port_ipv_4_config: Union[Unset, OsgWanPortIpv4ConfigVO]
        if isinstance(_wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = UNSET
        else:
            wan_port_ipv_4_config = OsgWanPortIpv4ConfigVO.from_dict(_wan_port_ipv_4_config)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        gateway_wan_status_entity = cls(
            port=port,
            name=name,
            port_desc=port_desc,
            status=status,
            internet_state=internet_state,
            wan_port_ipv_6_config=wan_port_ipv_6_config,
            wan_port_ipv_4_config=wan_port_ipv_4_config,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            latency=latency,
            loss=loss,
        )

        gateway_wan_status_entity.additional_properties = d
        return gateway_wan_status_entity

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
