from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteUserVO")


@_attrs_define
class DeleteUserVO:
    """
    Attributes:
        force_delete (Union[Unset, bool]): Force delete target user. If false, target user can not be deleted, when
            target user has child users. If true, target user will be deleted anyway. Target user's child users will be
            root's child user.
    """

    force_delete: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        force_delete = self.force_delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force_delete is not UNSET:
            field_dict["forceDelete"] = force_delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        force_delete = d.pop("forceDelete", UNSET)

        delete_user_vo = cls(
            force_delete=force_delete,
        )

        delete_user_vo.additional_properties = d
        return delete_user_vo

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
