from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalResOpenApiVO")


@_attrs_define
class PortalResOpenApiVO:
    """
    Attributes:
        id (Union[Unset, str]): Portal id
        name (Union[Unset, str]): Portal name
        enable (Union[Unset, bool]): Is the portal enable.
        ssid_list (Union[Unset, List[str]]): The ssid list of the portal binding.
        network_list (Union[Unset, List[str]]): IThe network id list of the portal binding.
        auth_type (Union[Unset, int]): The type of Authentication. 0:NO_AUTH, 1:SIMPLE_PASSWORD, 2:EXTERNAL_RADIUS,

            4:EXTERNAL_PORTAL_SERVER, 7:FACEBOOK, 11:HOTSPOT
        hotspot_types (Union[Unset, List[int]]): The enable types of hotspot. 3:VOUCHER, 5:LOCAL_USER

            6:SMS, 8: HOTSPOT_RADIUS, 12:FORM_AUTH
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    ssid_list: Union[Unset, List[str]] = UNSET
    network_list: Union[Unset, List[str]] = UNSET
    auth_type: Union[Unset, int] = UNSET
    hotspot_types: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        enable = self.enable
        ssid_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = self.ssid_list

        network_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        auth_type = self.auth_type
        hotspot_types: Union[Unset, List[int]] = UNSET
        if not isinstance(self.hotspot_types, Unset):
            hotspot_types = self.hotspot_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enable is not UNSET:
            field_dict["enable"] = enable
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if hotspot_types is not UNSET:
            field_dict["hotspotTypes"] = hotspot_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enable = d.pop("enable", UNSET)

        ssid_list = cast(List[str], d.pop("ssidList", UNSET))

        network_list = cast(List[str], d.pop("networkList", UNSET))

        auth_type = d.pop("authType", UNSET)

        hotspot_types = cast(List[int], d.pop("hotspotTypes", UNSET))

        portal_res_open_api_vo = cls(
            id=id,
            name=name,
            enable=enable,
            ssid_list=ssid_list,
            network_list=network_list,
            auth_type=auth_type,
            hotspot_types=hotspot_types,
        )

        portal_res_open_api_vo.additional_properties = d
        return portal_res_open_api_vo

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
