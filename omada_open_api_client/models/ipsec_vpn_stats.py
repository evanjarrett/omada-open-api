from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsecVpnStats")


@_attrs_define
class IpsecVpnStats:
    """
    Attributes:
        site (Union[Unset, str]): site
        name (Union[Unset, str]): VPN name
        id (Union[Unset, int]): VPN ID
        status (Union[Unset, bool]): VPN enable
        direction (Union[Unset, str]): SA direction: in/out
        local_peer_ip (Union[Unset, str]): IP address of the local peer
        remote_peer_ip (Union[Unset, str]): IP address of the remote peer
        local_sa (Union[Unset, str]): Local network segment of SA Cover, such as
        remote_sa (Union[Unset, str]): Remote network segment of SA Cover
    """

    site: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    status: Union[Unset, bool] = UNSET
    direction: Union[Unset, str] = UNSET
    local_peer_ip: Union[Unset, str] = UNSET
    remote_peer_ip: Union[Unset, str] = UNSET
    local_sa: Union[Unset, str] = UNSET
    remote_sa: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site = self.site
        name = self.name
        id = self.id
        status = self.status
        direction = self.direction
        local_peer_ip = self.local_peer_ip
        remote_peer_ip = self.remote_peer_ip
        local_sa = self.local_sa
        remote_sa = self.remote_sa

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if direction is not UNSET:
            field_dict["direction"] = direction
        if local_peer_ip is not UNSET:
            field_dict["localPeerIp"] = local_peer_ip
        if remote_peer_ip is not UNSET:
            field_dict["remotePeerIp"] = remote_peer_ip
        if local_sa is not UNSET:
            field_dict["localSa"] = local_sa
        if remote_sa is not UNSET:
            field_dict["remoteSa"] = remote_sa

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site = d.pop("site", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        direction = d.pop("direction", UNSET)

        local_peer_ip = d.pop("localPeerIp", UNSET)

        remote_peer_ip = d.pop("remotePeerIp", UNSET)

        local_sa = d.pop("localSa", UNSET)

        remote_sa = d.pop("remoteSa", UNSET)

        ipsec_vpn_stats = cls(
            site=site,
            name=name,
            id=id,
            status=status,
            direction=direction,
            local_peer_ip=local_peer_ip,
            remote_peer_ip=remote_peer_ip,
            local_sa=local_sa,
            remote_sa=remote_sa,
        )

        ipsec_vpn_stats.additional_properties = d
        return ipsec_vpn_stats

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
