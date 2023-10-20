from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeshSettingVO")


@_attrs_define
class MeshSettingVO:
    """
    Attributes:
        mesh_enable (bool):
        auto_failover_enable (Union[Unset, bool]):
        def_gateway_enable (Union[Unset, bool]):
        gateway (Union[Unset, str]):
        full_sector (Union[Unset, bool]):
    """

    mesh_enable: bool
    auto_failover_enable: Union[Unset, bool] = UNSET
    def_gateway_enable: Union[Unset, bool] = UNSET
    gateway: Union[Unset, str] = UNSET
    full_sector: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mesh_enable = self.mesh_enable
        auto_failover_enable = self.auto_failover_enable
        def_gateway_enable = self.def_gateway_enable
        gateway = self.gateway
        full_sector = self.full_sector

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meshEnable": mesh_enable,
            }
        )
        if auto_failover_enable is not UNSET:
            field_dict["autoFailoverEnable"] = auto_failover_enable
        if def_gateway_enable is not UNSET:
            field_dict["defGatewayEnable"] = def_gateway_enable
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if full_sector is not UNSET:
            field_dict["fullSector"] = full_sector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mesh_enable = d.pop("meshEnable")

        auto_failover_enable = d.pop("autoFailoverEnable", UNSET)

        def_gateway_enable = d.pop("defGatewayEnable", UNSET)

        gateway = d.pop("gateway", UNSET)

        full_sector = d.pop("fullSector", UNSET)

        mesh_setting_vo = cls(
            mesh_enable=mesh_enable,
            auto_failover_enable=auto_failover_enable,
            def_gateway_enable=def_gateway_enable,
            gateway=gateway,
            full_sector=full_sector,
        )

        mesh_setting_vo.additional_properties = d
        return mesh_setting_vo

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
