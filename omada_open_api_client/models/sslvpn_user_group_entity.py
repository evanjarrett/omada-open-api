from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sslvpn_resource_brief_group_entity import SSLVPNResourceBriefGroupEntity


T = TypeVar("T", bound="SSLVPNUserGroupEntity")


@_attrs_define
class SSLVPNUserGroupEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN user group
        id (Union[Unset, str]): Id of the SSL VPN user group
        resource_group_list (Union[Unset, List['SSLVPNResourceBriefGroupEntity']]): Resource group list of the SSL VPN
            user group
        user_list (Union[Unset, List[str]]): User list of the SSL VPN user group
        user_number (Union[Unset, int]): User number of the SSL VPN user group
    """

    name: str
    id: Union[Unset, str] = UNSET
    resource_group_list: Union[Unset, List["SSLVPNResourceBriefGroupEntity"]] = UNSET
    user_list: Union[Unset, List[str]] = UNSET
    user_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        resource_group_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resource_group_list, Unset):
            resource_group_list = []
            for resource_group_list_item_data in self.resource_group_list:
                resource_group_list_item = resource_group_list_item_data.to_dict()

                resource_group_list.append(resource_group_list_item)

        user_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_list, Unset):
            user_list = self.user_list

        user_number = self.user_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resource_group_list is not UNSET:
            field_dict["resourceGroupList"] = resource_group_list
        if user_list is not UNSET:
            field_dict["userList"] = user_list
        if user_number is not UNSET:
            field_dict["userNumber"] = user_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sslvpn_resource_brief_group_entity import SSLVPNResourceBriefGroupEntity

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        resource_group_list = []
        _resource_group_list = d.pop("resourceGroupList", UNSET)
        for resource_group_list_item_data in _resource_group_list or []:
            resource_group_list_item = SSLVPNResourceBriefGroupEntity.from_dict(resource_group_list_item_data)

            resource_group_list.append(resource_group_list_item)

        user_list = cast(List[str], d.pop("userList", UNSET))

        user_number = d.pop("userNumber", UNSET)

        sslvpn_user_group_entity = cls(
            name=name,
            id=id,
            resource_group_list=resource_group_list,
            user_list=user_list,
            user_number=user_number,
        )

        sslvpn_user_group_entity.additional_properties = d
        return sslvpn_user_group_entity

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
