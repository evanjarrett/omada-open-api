from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_port_config_entity import GatewayPortConfigEntity


T = TypeVar("T", bound="GatewayPortsConfigEntity")


@_attrs_define
class GatewayPortsConfigEntity:
    """
    Attributes:
        ports_config (Union[Unset, List['GatewayPortConfigEntity']]): gateway port config entity
    """

    ports_config: Union[Unset, List["GatewayPortConfigEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ports_config: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ports_config, Unset):
            ports_config = []
            for ports_config_item_data in self.ports_config:
                ports_config_item = ports_config_item_data.to_dict()

                ports_config.append(ports_config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ports_config is not UNSET:
            field_dict["portsConfig"] = ports_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_port_config_entity import GatewayPortConfigEntity

        d = src_dict.copy()
        ports_config = []
        _ports_config = d.pop("portsConfig", UNSET)
        for ports_config_item_data in _ports_config or []:
            ports_config_item = GatewayPortConfigEntity.from_dict(ports_config_item_data)

            ports_config.append(ports_config_item)

        gateway_ports_config_entity = cls(
            ports_config=ports_config,
        )

        gateway_ports_config_entity.additional_properties = d
        return gateway_ports_config_entity

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
