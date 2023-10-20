from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenDetailVO")


@_attrs_define
class AccessTokenDetailVO:
    """
    Attributes:
        access_token (Union[Unset, str]): Access Token
        token_type (Union[Unset, str]): Token Type
        expires_in (Union[Unset, int]): Time until token expires in seconds.
        refresh_token (Union[Unset, str]): Token used to refresh this access token.
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        token_type = self.token_type
        expires_in = self.expires_in
        refresh_token = self.refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if token_type is not UNSET:
            field_dict["tokenType"] = token_type
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("accessToken", UNSET)

        token_type = d.pop("tokenType", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        access_token_detail_vo = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_token=refresh_token,
        )

        access_token_detail_vo.additional_properties = d
        return access_token_detail_vo

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
