from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSLVPNLockEntity")


@_attrs_define
class SSLVPNLockEntity:
    """
    Attributes:
        type (int): Type of the SSL VPN lock
        total_lock_time (int): Total lock time of the SSL VPN lock
        id (Union[Unset, str]): Id of the SSL VPN lock
        username (Union[Unset, str]): Username of the SSL VPN lock
        ip (Union[Unset, str]): Ip of the SSL VPN lock
        left_lock_time (Union[Unset, int]): Left lock time of the SSL VPN lock
    """

    type: int
    total_lock_time: int
    id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    left_lock_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        total_lock_time = self.total_lock_time
        id = self.id
        username = self.username
        ip = self.ip
        left_lock_time = self.left_lock_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "totalLockTime": total_lock_time,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if ip is not UNSET:
            field_dict["ip"] = ip
        if left_lock_time is not UNSET:
            field_dict["leftLockTime"] = left_lock_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        total_lock_time = d.pop("totalLockTime")

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        ip = d.pop("ip", UNSET)

        left_lock_time = d.pop("leftLockTime", UNSET)

        sslvpn_lock_entity = cls(
            type=type,
            total_lock_time=total_lock_time,
            id=id,
            username=username,
            ip=ip,
            left_lock_time=left_lock_time,
        )

        sslvpn_lock_entity.additional_properties = d
        return sslvpn_lock_entity

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
