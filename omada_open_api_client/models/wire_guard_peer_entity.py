from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardPeerEntity")


@_attrs_define
class WireGuardPeerEntity:
    """
    Attributes:
        status (bool): Status of the WireGuard peer
        interface_id (str): Interface id of the WireGuard peer
        allow_address (List[str]): Allow address of the WireGuard peer
        id (Union[Unset, str]): Id of the WireGuard peer
        name (Union[Unset, str]): Name of the WireGuard peer
        interface_name (Union[Unset, str]): Interface name of the WireGuard peer
        public_key (Union[Unset, str]): Public key of the WireGuard peer
        end_point (Union[Unset, str]): End point of the WireGuard peer
        end_point_port (Union[Unset, int]): End point port of the WireGuard peer
        pre_shared_key (Union[Unset, str]): Pre shared key of the WireGuard peer
        keep_alive (Union[Unset, int]): Keep alive of the WireGuard peer
        comment (Union[Unset, str]): Comment of the WireGuard peer
    """

    status: bool
    interface_id: str
    allow_address: List[str]
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    end_point: Union[Unset, str] = UNSET
    end_point_port: Union[Unset, int] = UNSET
    pre_shared_key: Union[Unset, str] = UNSET
    keep_alive: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        interface_id = self.interface_id
        allow_address = self.allow_address

        id = self.id
        name = self.name
        interface_name = self.interface_name
        public_key = self.public_key
        end_point = self.end_point
        end_point_port = self.end_point_port
        pre_shared_key = self.pre_shared_key
        keep_alive = self.keep_alive
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "interfaceId": interface_id,
                "allowAddress": allow_address,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if end_point_port is not UNSET:
            field_dict["endPointPort"] = end_point_port
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        interface_id = d.pop("interfaceId")

        allow_address = cast(List[str], d.pop("allowAddress"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        public_key = d.pop("publicKey", UNSET)

        end_point = d.pop("endPoint", UNSET)

        end_point_port = d.pop("endPointPort", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        comment = d.pop("comment", UNSET)

        wire_guard_peer_entity = cls(
            status=status,
            interface_id=interface_id,
            allow_address=allow_address,
            id=id,
            name=name,
            interface_name=interface_name,
            public_key=public_key,
            end_point=end_point,
            end_point_port=end_point_port,
            pre_shared_key=pre_shared_key,
            keep_alive=keep_alive,
            comment=comment,
        )

        wire_guard_peer_entity.additional_properties = d
        return wire_guard_peer_entity

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
