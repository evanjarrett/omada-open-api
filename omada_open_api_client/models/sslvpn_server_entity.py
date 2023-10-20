from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSLVPNServerEntity")


@_attrs_define
class SSLVPNServerEntity:
    """
    Attributes:
        status (bool): Status of the SSL VPN server.
        id (Union[Unset, str]): Id of the SSL VPN server.
        wan_port (Union[Unset, str]): WanPort of the SSL VPN server.
        wan_ip (Union[Unset, str]): WanIp of the SSL VPN server.
        ip_pool_start (Union[Unset, str]): The start ip of the ip pool.
        ip_pool_end (Union[Unset, str]): The end ip of the ip pool.
        primary_dns (Union[Unset, str]): Primary Dns Server of the SSL VPN server.
        secondary_dns (Union[Unset, str]): Secondary Dns Server of the SSL VPN server.
        service_port (Union[Unset, int]): Service port of the SSL VPN server.
        auth_type (Union[Unset, int]): Authentication type of the SSL VPN server, 0 represents local, 1 represents
            radius.
    """

    status: bool
    id: Union[Unset, str] = UNSET
    wan_port: Union[Unset, str] = UNSET
    wan_ip: Union[Unset, str] = UNSET
    ip_pool_start: Union[Unset, str] = UNSET
    ip_pool_end: Union[Unset, str] = UNSET
    primary_dns: Union[Unset, str] = UNSET
    secondary_dns: Union[Unset, str] = UNSET
    service_port: Union[Unset, int] = UNSET
    auth_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        id = self.id
        wan_port = self.wan_port
        wan_ip = self.wan_ip
        ip_pool_start = self.ip_pool_start
        ip_pool_end = self.ip_pool_end
        primary_dns = self.primary_dns
        secondary_dns = self.secondary_dns
        service_port = self.service_port
        auth_type = self.auth_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if wan_port is not UNSET:
            field_dict["wanPort"] = wan_port
        if wan_ip is not UNSET:
            field_dict["wanIp"] = wan_ip
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        id = d.pop("id", UNSET)

        wan_port = d.pop("wanPort", UNSET)

        wan_ip = d.pop("wanIp", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        service_port = d.pop("servicePort", UNSET)

        auth_type = d.pop("authType", UNSET)

        sslvpn_server_entity = cls(
            status=status,
            id=id,
            wan_port=wan_port,
            wan_ip=wan_ip,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            service_port=service_port,
            auth_type=auth_type,
        )

        sslvpn_server_entity.additional_properties = d
        return sslvpn_server_entity

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
