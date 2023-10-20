from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSLVPNUserEntity")


@_attrs_define
class SSLVPNUserEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN user
        status (bool): Status of the SSL VPN user
        password (str): Password of the SSL VPN user
        validity (str): Validity of the SSL VPN user
        concurrent_number (int): Concurrent number of the SSL VPN user
        id (Union[Unset, str]): Id of the SSL VPN user
        group_id (Union[Unset, str]): Group id of the SSL VPN user
        group_name (Union[Unset, str]): Group name of the SSL VPN user
        available (Union[Unset, bool]): Available of the SSL VPN user
    """

    name: str
    status: bool
    password: str
    validity: str
    concurrent_number: int
    id: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    available: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status = self.status
        password = self.password
        validity = self.validity
        concurrent_number = self.concurrent_number
        id = self.id
        group_id = self.group_id
        group_name = self.group_name
        available = self.available

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "password": password,
                "validity": validity,
                "concurrentNumber": concurrent_number,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        status = d.pop("status")

        password = d.pop("password")

        validity = d.pop("validity")

        concurrent_number = d.pop("concurrentNumber")

        id = d.pop("id", UNSET)

        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        available = d.pop("available", UNSET)

        sslvpn_user_entity = cls(
            name=name,
            status=status,
            password=password,
            validity=validity,
            concurrent_number=concurrent_number,
            id=id,
            group_id=group_id,
            group_name=group_name,
            available=available,
        )

        sslvpn_user_entity.additional_properties = d
        return sslvpn_user_entity

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
