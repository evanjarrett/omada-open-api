from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PortInfoEntity")


@_attrs_define
class PortInfoEntity:
    """portList

    Attributes:
        port (int): port
        name (str): port name
        profile_id (str): profileId
        profile_name (str): profileName
    """

    port: int
    name: str
    profile_id: str
    profile_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port = self.port
        name = self.name
        profile_id = self.profile_id
        profile_name = self.profile_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "name": name,
                "profileId": profile_id,
                "profileName": profile_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        port = d.pop("port")

        name = d.pop("name")

        profile_id = d.pop("profileId")

        profile_name = d.pop("profileName")

        port_info_entity = cls(
            port=port,
            name=name,
            profile_id=profile_id,
            profile_name=profile_name,
        )

        port_info_entity.additional_properties = d
        return port_info_entity

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
