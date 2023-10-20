from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDetailVO")


@_attrs_define
class UserDetailVO:
    """
    Attributes:
        id (Union[Unset, str]): User id
        type (Union[Unset, int]): Type of user, 0:local user; 1: cloud user
        role_id (Union[Unset, str]): User role id
        role_name (Union[Unset, str]): user bind role name
        name (Union[Unset, str]): user name
        email (Union[Unset, str]): User email
        omadac_id (Union[Unset, str]): Omadac id
        verified (Union[Unset, bool]): Whether this cloud user has verified
        alert (Union[Unset, bool]): Whether this user want to receive alert emails
        all_site (Union[Unset, bool]): Whether user has all site permission, including new created site
        site_ids (Union[Unset, List[str]]): User site privilege list
        parent_user_id (Union[Unset, str]): User's parernt user id
        favorites (Union[Unset, List[str]]): User favorite site list
        incident_notification (Union[Unset, bool]): incident notification
        user_level (Union[Unset, int]): User level. 0:standard user; 1:customer user; 2:msp user
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    role_id: Union[Unset, str] = UNSET
    role_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    omadac_id: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    alert: Union[Unset, bool] = UNSET
    all_site: Union[Unset, bool] = UNSET
    site_ids: Union[Unset, List[str]] = UNSET
    parent_user_id: Union[Unset, str] = UNSET
    favorites: Union[Unset, List[str]] = UNSET
    incident_notification: Union[Unset, bool] = UNSET
    user_level: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        role_id = self.role_id
        role_name = self.role_name
        name = self.name
        email = self.email
        omadac_id = self.omadac_id
        verified = self.verified
        alert = self.alert
        all_site = self.all_site
        site_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.site_ids, Unset):
            site_ids = self.site_ids

        parent_user_id = self.parent_user_id
        favorites: Union[Unset, List[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        incident_notification = self.incident_notification
        user_level = self.user_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if alert is not UNSET:
            field_dict["alert"] = alert
        if all_site is not UNSET:
            field_dict["allSite"] = all_site
        if site_ids is not UNSET:
            field_dict["siteIds"] = site_ids
        if parent_user_id is not UNSET:
            field_dict["parentUserId"] = parent_user_id
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if incident_notification is not UNSET:
            field_dict["incidentNotification"] = incident_notification
        if user_level is not UNSET:
            field_dict["userLevel"] = user_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        verified = d.pop("verified", UNSET)

        alert = d.pop("alert", UNSET)

        all_site = d.pop("allSite", UNSET)

        site_ids = cast(List[str], d.pop("siteIds", UNSET))

        parent_user_id = d.pop("parentUserId", UNSET)

        favorites = cast(List[str], d.pop("favorites", UNSET))

        incident_notification = d.pop("incidentNotification", UNSET)

        user_level = d.pop("userLevel", UNSET)

        user_detail_vo = cls(
            id=id,
            type=type,
            role_id=role_id,
            role_name=role_name,
            name=name,
            email=email,
            omadac_id=omadac_id,
            verified=verified,
            alert=alert,
            all_site=all_site,
            site_ids=site_ids,
            parent_user_id=parent_user_id,
            favorites=favorites,
            incident_notification=incident_notification,
            user_level=user_level,
        )

        user_detail_vo.additional_properties = d
        return user_detail_vo

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
