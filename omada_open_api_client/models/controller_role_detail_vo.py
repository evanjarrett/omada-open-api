from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_role_vo import ControllerRoleVO


T = TypeVar("T", bound="ControllerRoleDetailVO")


@_attrs_define
class ControllerRoleDetailVO:
    """
    Attributes:
        id (Union[Unset, str]): Role Id
        name (Union[Unset, str]): Role Name
        type (Union[Unset, int]): Role Type
        default_role (Union[Unset, bool]): Whether role is default role
        source (Union[Unset, int]): Role created resource. 0: default; 1:create by standard controller or customer
            controller; 2: create by MSP
        privilege (Union[Unset, ControllerRoleVO]): role privilege
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    default_role: Union[Unset, bool] = UNSET
    source: Union[Unset, int] = UNSET
    privilege: Union[Unset, "ControllerRoleVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type
        default_role = self.default_role
        source = self.source
        privilege: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if default_role is not UNSET:
            field_dict["defaultRole"] = default_role
        if source is not UNSET:
            field_dict["source"] = source
        if privilege is not UNSET:
            field_dict["privilege"] = privilege

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_role_vo import ControllerRoleVO

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        default_role = d.pop("defaultRole", UNSET)

        source = d.pop("source", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: Union[Unset, ControllerRoleVO]
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = ControllerRoleVO.from_dict(_privilege)

        controller_role_detail_vo = cls(
            id=id,
            name=name,
            type=type,
            default_role=default_role,
            source=source,
            privilege=privilege,
        )

        controller_role_detail_vo.additional_properties = d
        return controller_role_detail_vo

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
