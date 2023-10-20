from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardEntity")


@_attrs_define
class WireGuardEntity:
    """
    Attributes:
        name (str): Name of the WireGuard
        status (bool): Status of the WireGuard
        mtu (int): Mtu of the WireGuard
        listen_port (int): Listen port of the WireGuard
        private_key (str): Private key of the WireGuard
        local_ip (str): Local ip of the WireGuard
        id (Union[Unset, str]): Id of the WireGuard
        public_key (Union[Unset, str]): Public key of the WireGuard
    """

    name: str
    status: bool
    mtu: int
    listen_port: int
    private_key: str
    local_ip: str
    id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status = self.status
        mtu = self.mtu
        listen_port = self.listen_port
        private_key = self.private_key
        local_ip = self.local_ip
        id = self.id
        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "mtu": mtu,
                "listenPort": listen_port,
                "privateKey": private_key,
                "localIp": local_ip,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        status = d.pop("status")

        mtu = d.pop("mtu")

        listen_port = d.pop("listenPort")

        private_key = d.pop("privateKey")

        local_ip = d.pop("localIp")

        id = d.pop("id", UNSET)

        public_key = d.pop("publicKey", UNSET)

        wire_guard_entity = cls(
            name=name,
            status=status,
            mtu=mtu,
            listen_port=listen_port,
            private_key=private_key,
            local_ip=local_ip,
            id=id,
            public_key=public_key,
        )

        wire_guard_entity.additional_properties = d
        return wire_guard_entity

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
