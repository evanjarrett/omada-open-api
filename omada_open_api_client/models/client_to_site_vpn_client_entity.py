from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="ClientToSiteVPNClientEntity")


@_attrs_define
class ClientToSiteVPNClientEntity:
    """
    Attributes:
        name (str): Name of the VPN.
        id (Union[Unset, str]): Id of the VPN.
        status (Union[Unset, bool]): Status of the VPN
        mode (Union[Unset, int]): Mode of the VPN, only for server openVPN, 0 represents certification, 1 represents
            certification+account.
        remote_site (Union[Unset, str]): Remote site of the VPN
        remote_ip (Union[Unset, str]): Remote ip of the VPN
        remote_subnet (Union[Unset, List['IPSubnetsVO']]): Remote subnet of the VPN.
        network_type (Union[Unset, int]): Network type of the VPN, 0 represents network list, 1 represents custom
            networks.
        network_list (Union[Unset, List[str]]): Network list of the VPN.
        custom_network (Union[Unset, List['IPSubnetsVO']]): Custom networks of the VPN.
        pre_shared_key (Union[Unset, str]): Pre-shared key of the VPN.
        wan (Union[Unset, List[str]]): Wan list of the VPN.
        client_vpn_type (Union[Unset, int]): Client Vpn type of the VPN, 0 represents L2TP, 1 represents PPTP, 2
            represents IPSec, 3 represents OpenVPN.
        encryption (Union[Unset, int]): Encryption of the VPN, 0 represents Encrypted, 1 represents Unencrypted.
        working_mode (Union[Unset, int]): Working mode of the VPN, 0 represents NAT, 1 represents Routing.
        client_user_name (Union[Unset, str]): Client username of the VPN
        client_password (Union[Unset, str]): Client password of the VPN
    """

    name: str
    id: Union[Unset, str] = UNSET
    status: Union[Unset, bool] = UNSET
    mode: Union[Unset, int] = UNSET
    remote_site: Union[Unset, str] = UNSET
    remote_ip: Union[Unset, str] = UNSET
    remote_subnet: Union[Unset, List["IPSubnetsVO"]] = UNSET
    network_type: Union[Unset, int] = UNSET
    network_list: Union[Unset, List[str]] = UNSET
    custom_network: Union[Unset, List["IPSubnetsVO"]] = UNSET
    pre_shared_key: Union[Unset, str] = UNSET
    wan: Union[Unset, List[str]] = UNSET
    client_vpn_type: Union[Unset, int] = UNSET
    encryption: Union[Unset, int] = UNSET
    working_mode: Union[Unset, int] = UNSET
    client_user_name: Union[Unset, str] = UNSET
    client_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        status = self.status
        mode = self.mode
        remote_site = self.remote_site
        remote_ip = self.remote_ip
        remote_subnet: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = []
            for remote_subnet_item_data in self.remote_subnet:
                remote_subnet_item = remote_subnet_item_data.to_dict()

                remote_subnet.append(remote_subnet_item)

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
        working_mode = self.working_mode
        client_user_name = self.client_user_name
        client_password = self.client_password

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
        if mode is not UNSET:
            field_dict["mode"] = mode
        if remote_site is not UNSET:
            field_dict["remoteSite"] = remote_site
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
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
        if working_mode is not UNSET:
            field_dict["workingMode"] = working_mode
        if client_user_name is not UNSET:
            field_dict["clientUserName"] = client_user_name
        if client_password is not UNSET:
            field_dict["clientPassword"] = client_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        mode = d.pop("mode", UNSET)

        remote_site = d.pop("remoteSite", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        remote_subnet = []
        _remote_subnet = d.pop("remoteSubnet", UNSET)
        for remote_subnet_item_data in _remote_subnet or []:
            remote_subnet_item = IPSubnetsVO.from_dict(remote_subnet_item_data)

            remote_subnet.append(remote_subnet_item)

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

        working_mode = d.pop("workingMode", UNSET)

        client_user_name = d.pop("clientUserName", UNSET)

        client_password = d.pop("clientPassword", UNSET)

        client_to_site_vpn_client_entity = cls(
            name=name,
            id=id,
            status=status,
            mode=mode,
            remote_site=remote_site,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            pre_shared_key=pre_shared_key,
            wan=wan,
            client_vpn_type=client_vpn_type,
            encryption=encryption,
            working_mode=working_mode,
            client_user_name=client_user_name,
            client_password=client_password,
        )

        client_to_site_vpn_client_entity.additional_properties = d
        return client_to_site_vpn_client_entity

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
