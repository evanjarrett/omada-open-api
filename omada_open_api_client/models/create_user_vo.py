from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserVO")


@_attrs_define
class CreateUserVO:
    """
    Attributes:
        type (int): type of user, 0 for local user, 1 for cloud user
        role_id (str): role id of user
        name (str): user name. When creating cloud user, you should set TP-LINK ID
        all_site (bool): Whether user has all site permission, including new created site
        password (Union[Unset, str]): password of local user
        email (Union[Unset, str]): email of user
        alert (Union[Unset, bool]): Whether this user want to receive alert emails
        incident_notification (Union[Unset, bool]): incident notification
        sites (Union[Unset, List[str]]): User site privilege list
    """

    type: int
    role_id: str
    name: str
    all_site: bool
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    alert: Union[Unset, bool] = UNSET
    incident_notification: Union[Unset, bool] = UNSET
    sites: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        role_id = self.role_id
        name = self.name
        all_site = self.all_site
        password = self.password
        email = self.email
        alert = self.alert
        incident_notification = self.incident_notification
        sites: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "roleId": role_id,
                "name": name,
                "allSite": all_site,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if alert is not UNSET:
            field_dict["alert"] = alert
        if incident_notification is not UNSET:
            field_dict["incidentNotification"] = incident_notification
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        role_id = d.pop("roleId")

        name = d.pop("name")

        all_site = d.pop("allSite")

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        alert = d.pop("alert", UNSET)

        incident_notification = d.pop("incidentNotification", UNSET)

        sites = cast(List[str], d.pop("sites", UNSET))

        create_user_vo = cls(
            type=type,
            role_id=role_id,
            name=name,
            all_site=all_site,
            password=password,
            email=email,
            alert=alert,
            incident_notification=incident_notification,
            sites=sites,
        )

        create_user_vo.additional_properties = d
        return create_user_vo

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
