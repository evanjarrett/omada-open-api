from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_setting_vo import MeshSettingVO


T = TypeVar("T", bound="SiteSettingmesh")


@_attrs_define
class SiteSettingmesh:
    """
    Attributes:
        mesh (Union[Unset, MeshSettingVO]):
    """

    mesh: Union[Unset, "MeshSettingVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mesh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mesh is not UNSET:
            field_dict["mesh"] = mesh

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mesh_setting_vo import MeshSettingVO

        d = src_dict.copy()
        _mesh = d.pop("mesh", UNSET)
        mesh: Union[Unset, MeshSettingVO]
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = MeshSettingVO.from_dict(_mesh)

        site_settingmesh = cls(
            mesh=mesh,
        )

        site_settingmesh.additional_properties = d
        return site_settingmesh

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
