from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyUserVO")


@_attrs_define
class ModifyUserVO:
    """
    Attributes:
        role_id (str): role id of user
        name (str): user name. When creating cloud user, you should set TP-LINK ID
        sites (List[str]): user site privilege list
        all_site (bool): whether user has all site privilege
        password (Union[Unset, str]): password of local user
        email (Union[Unset, str]): email of user
        alert (Union[Unset, bool]): alert email
        force_modify (Union[Unset, bool]): force modify
        incident_notification (Union[Unset, bool]): incident notification
    """

    role_id: str
    name: str
    sites: List[str]
    all_site: bool
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    alert: Union[Unset, bool] = UNSET
    force_modify: Union[Unset, bool] = UNSET
    incident_notification: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id
        name = self.name
        sites = self.sites

        all_site = self.all_site
        password = self.password
        email = self.email
        alert = self.alert
        force_modify = self.force_modify
        incident_notification = self.incident_notification

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roleId": role_id,
                "name": name,
                "sites": sites,
                "allSite": all_site,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if alert is not UNSET:
            field_dict["alert"] = alert
        if force_modify is not UNSET:
            field_dict["forceModify"] = force_modify
        if incident_notification is not UNSET:
            field_dict["incidentNotification"] = incident_notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("roleId")

        name = d.pop("name")

        sites = cast(List[str], d.pop("sites"))

        all_site = d.pop("allSite")

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        alert = d.pop("alert", UNSET)

        force_modify = d.pop("forceModify", UNSET)

        incident_notification = d.pop("incidentNotification", UNSET)

        modify_user_vo = cls(
            role_id=role_id,
            name=name,
            sites=sites,
            all_site=all_site,
            password=password,
            email=email,
            alert=alert,
            force_modify=force_modify,
            incident_notification=incident_notification,
        )

        modify_user_vo.additional_properties = d
        return modify_user_vo

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
