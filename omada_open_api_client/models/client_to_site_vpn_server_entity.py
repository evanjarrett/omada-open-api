from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="ClientToSiteVPNServerEntity")


@_attrs_define
class ClientToSiteVPNServerEntity:
    """
    Attributes:
        name (str): Name of the VPN.
        id (Union[Unset, str]): Id of the VPN.
        status (Union[Unset, bool]): Status of the VPN.
        account_password (Union[Unset, bool]): Account password of the VPN, only for server openVPN.
        tunnel_mode (Union[Unset, int]): Tunnel mode of the VPN, only for server openVPN, 0 represents split, 1
            represents full.
        remote_ip (Union[Unset, str]): Remote ip of the VPN
        network_type (Union[Unset, int]): Network type of the VPN, 0 represents network list, 1 represents custom
            networks.
        network_list (Union[Unset, List[str]]): Network list of the VPN.
        custom_network (Union[Unset, List['IPSubnetsVO']]): Custom networks of the VPN.
        pre_shared_key (Union[Unset, str]): Pre-shared key of the VPN.
        wan (Union[Unset, List[str]]): Wan list of the VPN.
        client_vpn_type (Union[Unset, int]): Client Vpn type of the VPN, 0 represents L2TP, 1 represents PPTP, 2
            represents IPSec, 3 represents OpenVPN.
        encryption (Union[Unset, int]): Encryption of the VPN, 0 represents Encrypted, 1 represents Unencrypted.
        ip_pool_type (Union[Unset, int]): Ip pool type of the VPN, 0 represents Ip Address/Mask, 1 represents Ip Address
            Range.
        ip_pool_start (Union[Unset, str]): The start ip of the ip pool.
        ip_pool_end (Union[Unset, str]): The end ip of the ip pool.
        ip_pool (Union[Unset, IPSubnetsVO]): Custom networks of the VPN.
        primary_dns (Union[Unset, str]): Primary dns of the VPN.
        secondary_dns (Union[Unset, str]): Secondary dns of the VPN.
        service_type (Union[Unset, int]): Service type of the VPN.
        service_port (Union[Unset, int]): Service port of the VPN.
        auth_mode (Union[Unset, int]): Authentication mode of the VPN, 0 represents Local, 1 represents LDAP.
    """

    name: str
    id: Union[Unset, str] = UNSET
    status: Union[Unset, bool] = UNSET
    account_password: Union[Unset, bool] = UNSET
    tunnel_mode: Union[Unset, int] = UNSET
    remote_ip: Union[Unset, str] = UNSET
    network_type: Union[Unset, int] = UNSET
    network_list: Union[Unset, List[str]] = UNSET
    custom_network: Union[Unset, List["IPSubnetsVO"]] = UNSET
    pre_shared_key: Union[Unset, str] = UNSET
    wan: Union[Unset, List[str]] = UNSET
    client_vpn_type: Union[Unset, int] = UNSET
    encryption: Union[Unset, int] = UNSET
    ip_pool_type: Union[Unset, int] = UNSET
    ip_pool_start: Union[Unset, str] = UNSET
    ip_pool_end: Union[Unset, str] = UNSET
    ip_pool: Union[Unset, "IPSubnetsVO"] = UNSET
    primary_dns: Union[Unset, str] = UNSET
    secondary_dns: Union[Unset, str] = UNSET
    service_type: Union[Unset, int] = UNSET
    service_port: Union[Unset, int] = UNSET
    auth_mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        status = self.status
        account_password = self.account_password
        tunnel_mode = self.tunnel_mode
        remote_ip = self.remote_ip
        network_type = self.network_type
        network_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        custom_network: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_network, Unset):
            custom_network = []
            for custom_network_item_data in self.custom_network:
                custom_network_item = custom_network_item_data.to_dict()

                custom_network.append(custom_network_item)

        pre_shared_key = self.pre_shared_key
        wan: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wan, Unset):
            wan = self.wan

        client_vpn_type = self.client_vpn_type
        encryption = self.encryption
        ip_pool_type = self.ip_pool_type
        ip_pool_start = self.ip_pool_start
        ip_pool_end = self.ip_pool_end
        ip_pool: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_pool, Unset):
            ip_pool = self.ip_pool.to_dict()

        primary_dns = self.primary_dns
        secondary_dns = self.secondary_dns
        service_type = self.service_type
        service_port = self.service_port
        auth_mode = self.auth_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if account_password is not UNSET:
            field_dict["accountPassword"] = account_password
        if tunnel_mode is not UNSET:
            field_dict["tunnelMode"] = tunnel_mode
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if wan is not UNSET:
            field_dict["wan"] = wan
        if client_vpn_type is not UNSET:
            field_dict["clientVpnType"] = client_vpn_type
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if ip_pool_type is not UNSET:
            field_dict["ipPoolType"] = ip_pool_type
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if ip_pool is not UNSET:
            field_dict["ipPool"] = ip_pool
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        account_password = d.pop("accountPassword", UNSET)

        tunnel_mode = d.pop("tunnelMode", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(List[str], d.pop("networkList", UNSET))

        custom_network = []
        _custom_network = d.pop("customNetwork", UNSET)
        for custom_network_item_data in _custom_network or []:
            custom_network_item = IPSubnetsVO.from_dict(custom_network_item_data)

            custom_network.append(custom_network_item)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        wan = cast(List[str], d.pop("wan", UNSET))

        client_vpn_type = d.pop("clientVpnType", UNSET)

        encryption = d.pop("encryption", UNSET)

        ip_pool_type = d.pop("ipPoolType", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        _ip_pool = d.pop("ipPool", UNSET)
        ip_pool: Union[Unset, IPSubnetsVO]
        if isinstance(_ip_pool, Unset):
            ip_pool = UNSET
        else:
            ip_pool = IPSubnetsVO.from_dict(_ip_pool)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        service_type = d.pop("serviceType", UNSET)

        service_port = d.pop("servicePort", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        client_to_site_vpn_server_entity = cls(
            name=name,
            id=id,
            status=status,
            account_password=account_password,
            tunnel_mode=tunnel_mode,
            remote_ip=remote_ip,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            pre_shared_key=pre_shared_key,
            wan=wan,
            client_vpn_type=client_vpn_type,
            encryption=encryption,
            ip_pool_type=ip_pool_type,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            ip_pool=ip_pool,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            service_type=service_type,
            service_port=service_port,
            auth_mode=auth_mode,
        )

        client_to_site_vpn_server_entity.additional_properties = d
        return client_to_site_vpn_server_entity

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
