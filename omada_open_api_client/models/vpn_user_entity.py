from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="VPNUserEntity")


@_attrs_define
class VPNUserEntity:
    """
    Attributes:
        id (Union[Unset, str]): Id of the VPN user.
        username (Union[Unset, str]): Username of the VPN user.
        password (Union[Unset, str]): Password of the VPN user.
        protocol (Union[Unset, int]): Protocol of the VPN user, 0 represents L2TP or PPTP, 1 represents openVPN.
        client_mode (Union[Unset, int]): Client mode of the VPN user, 0 represents Client-To-Site, 1 represents Site-To-
            Site.
        max_connections (Union[Unset, int]): MaxConnections of the VPN user
        user_remote_subnets (Union[Unset, List['IPSubnetsVO']]): User remote subnets of the VPN user.
        servers (Union[Unset, List[str]]): Servers of the VPN user.
        local_ip (Union[Unset, str]): Local ip of the VPN user
        server_names (Union[Unset, str]): Server names of the VPN user.
    """

    id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    protocol: Union[Unset, int] = UNSET
    client_mode: Union[Unset, int] = UNSET
    max_connections: Union[Unset, int] = UNSET
    user_remote_subnets: Union[Unset, List["IPSubnetsVO"]] = UNSET
    servers: Union[Unset, List[str]] = UNSET
    local_ip: Union[Unset, str] = UNSET
    server_names: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        password = self.password
        protocol = self.protocol
        client_mode = self.client_mode
        max_connections = self.max_connections
        user_remote_subnets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_remote_subnets, Unset):
            user_remote_subnets = []
            for user_remote_subnets_item_data in self.user_remote_subnets:
                user_remote_subnets_item = user_remote_subnets_item_data.to_dict()

                user_remote_subnets.append(user_remote_subnets_item)

        servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        local_ip = self.local_ip
        server_names = self.server_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if client_mode is not UNSET:
            field_dict["clientMode"] = client_mode
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if user_remote_subnets is not UNSET:
            field_dict["userRemoteSubnets"] = user_remote_subnets
        if servers is not UNSET:
            field_dict["servers"] = servers
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if server_names is not UNSET:
            field_dict["serverNames"] = server_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        protocol = d.pop("protocol", UNSET)

        client_mode = d.pop("clientMode", UNSET)

        max_connections = d.pop("maxConnections", UNSET)

        user_remote_subnets = []
        _user_remote_subnets = d.pop("userRemoteSubnets", UNSET)
        for user_remote_subnets_item_data in _user_remote_subnets or []:
            user_remote_subnets_item = IPSubnetsVO.from_dict(user_remote_subnets_item_data)

            user_remote_subnets.append(user_remote_subnets_item)

        servers = cast(List[str], d.pop("servers", UNSET))

        local_ip = d.pop("localIp", UNSET)

        server_names = d.pop("serverNames", UNSET)

        vpn_user_entity = cls(
            id=id,
            username=username,
            password=password,
            protocol=protocol,
            client_mode=client_mode,
            max_connections=max_connections,
            user_remote_subnets=user_remote_subnets,
            servers=servers,
            local_ip=local_ip,
            server_names=server_names,
        )

        vpn_user_entity.additional_properties = d
        return vpn_user_entity

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
