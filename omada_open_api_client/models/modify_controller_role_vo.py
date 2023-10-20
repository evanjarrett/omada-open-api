from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_role_vo import ControllerRoleVO


T = TypeVar("T", bound="ModifyControllerRoleVO")


@_attrs_define
class ModifyControllerRoleVO:
    """
    Attributes:
        name (str): role name
        privilege (Union[Unset, ControllerRoleVO]): role privilege
    """

    name: str
    privilege: Union[Unset, "ControllerRoleVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        privilege: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if privilege is not UNSET:
            field_dict["privilege"] = privilege

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_role_vo import ControllerRoleVO

        d = src_dict.copy()
        name = d.pop("name")

        _privilege = d.pop("privilege", UNSET)
        privilege: Union[Unset, ControllerRoleVO]
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = ControllerRoleVO.from_dict(_privilege)

        modify_controller_role_vo = cls(
            name=name,
            privilege=privilege,
        )

        modify_controller_role_vo.additional_properties = d
        return modify_controller_role_vo

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
