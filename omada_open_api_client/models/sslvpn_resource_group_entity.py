from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sslvpn_resource_brief_entity import SSLVPNResourceBriefEntity


T = TypeVar("T", bound="SSLVPNResourceGroupEntity")


@_attrs_define
class SSLVPNResourceGroupEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN resource group
        id (Union[Unset, str]): Id of the SSL VPN resource group
        resources_list (Union[Unset, List['SSLVPNResourceBriefEntity']]): Resources list of the SSL VPN resource group
    """

    name: str
    id: Union[Unset, str] = UNSET
    resources_list: Union[Unset, List["SSLVPNResourceBriefEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        resources_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources_list, Unset):
            resources_list = []
            for resources_list_item_data in self.resources_list:
                resources_list_item = resources_list_item_data.to_dict()

                resources_list.append(resources_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resources_list is not UNSET:
            field_dict["resourcesList"] = resources_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sslvpn_resource_brief_entity import SSLVPNResourceBriefEntity

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        resources_list = []
        _resources_list = d.pop("resourcesList", UNSET)
        for resources_list_item_data in _resources_list or []:
            resources_list_item = SSLVPNResourceBriefEntity.from_dict(resources_list_item_data)

            resources_list.append(resources_list_item)

        sslvpn_resource_group_entity = cls(
            name=name,
            id=id,
            resources_list=resources_list,
        )

        sslvpn_resource_group_entity.additional_properties = d
        return sslvpn_resource_group_entity

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
