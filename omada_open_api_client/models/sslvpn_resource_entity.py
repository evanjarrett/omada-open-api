from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sslvpn_resource_brief_group_entity import SSLVPNResourceBriefGroupEntity


T = TypeVar("T", bound="SSLVPNResourceEntity")


@_attrs_define
class SSLVPNResourceEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN resource.
        type (int): Type of the SSL VPN resource, 0 represents ip, 1 represents domain.
        id (Union[Unset, str]): Id of the SSL VPN resource.
        resource_group_list (Union[Unset, List['SSLVPNResourceBriefGroupEntity']]): Resource group list of the SSL VPN
            resource.
        ip (Union[Unset, str]): Ip of the SSL VPN resource, exists when type is 0.
        mask (Union[Unset, str]): Mask of the SSL VPN resource, exists when type is 0.
        domain (Union[Unset, str]): Domain of the SSL VPN resource, exists when type is 1.
        protocol (Union[Unset, int]): Protocol of the SSL VPN resource.
        src_port_start (Union[Unset, int]): Start source port of the SSL VPN resource, exists when protocol is tcp or
            udp.
        src_port_end (Union[Unset, int]): End source port of the SSL VPN resource, exists when protocol is tcp or udp.
        dst_port_start (Union[Unset, int]): Start destination port of the SSL VPN resource, exists when protocol is tcp
            or udp.
        dst_port_end (Union[Unset, int]): End destination port of the SSL VPN resource, exists when protocol is tcp or
            udp.
        icmp_type (Union[Unset, int]): Icmp type of the SSL VPN resource, exists when protocol is icmp.
        icmp_code (Union[Unset, int]): Icmp code of the SSL VPN resource, exists when protocol is icmp.
        other_protocol (Union[Unset, int]): Other protocol of the SSL VPN resource.
    """

    name: str
    type: int
    id: Union[Unset, str] = UNSET
    resource_group_list: Union[Unset, List["SSLVPNResourceBriefGroupEntity"]] = UNSET
    ip: Union[Unset, str] = UNSET
    mask: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    protocol: Union[Unset, int] = UNSET
    src_port_start: Union[Unset, int] = UNSET
    src_port_end: Union[Unset, int] = UNSET
    dst_port_start: Union[Unset, int] = UNSET
    dst_port_end: Union[Unset, int] = UNSET
    icmp_type: Union[Unset, int] = UNSET
    icmp_code: Union[Unset, int] = UNSET
    other_protocol: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        id = self.id
        resource_group_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resource_group_list, Unset):
            resource_group_list = []
            for resource_group_list_item_data in self.resource_group_list:
                resource_group_list_item = resource_group_list_item_data.to_dict()

                resource_group_list.append(resource_group_list_item)

        ip = self.ip
        mask = self.mask
        domain = self.domain
        protocol = self.protocol
        src_port_start = self.src_port_start
        src_port_end = self.src_port_end
        dst_port_start = self.dst_port_start
        dst_port_end = self.dst_port_end
        icmp_type = self.icmp_type
        icmp_code = self.icmp_code
        other_protocol = self.other_protocol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resource_group_list is not UNSET:
            field_dict["resourceGroupList"] = resource_group_list
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mask is not UNSET:
            field_dict["mask"] = mask
        if domain is not UNSET:
            field_dict["domain"] = domain
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if src_port_start is not UNSET:
            field_dict["srcPortStart"] = src_port_start
        if src_port_end is not UNSET:
            field_dict["srcPortEnd"] = src_port_end
        if dst_port_start is not UNSET:
            field_dict["dstPortStart"] = dst_port_start
        if dst_port_end is not UNSET:
            field_dict["dstPortEnd"] = dst_port_end
        if icmp_type is not UNSET:
            field_dict["icmpType"] = icmp_type
        if icmp_code is not UNSET:
            field_dict["icmpCode"] = icmp_code
        if other_protocol is not UNSET:
            field_dict["otherProtocol"] = other_protocol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sslvpn_resource_brief_group_entity import SSLVPNResourceBriefGroupEntity

        d = src_dict.copy()
        name = d.pop("name")

        type = d.pop("type")

        id = d.pop("id", UNSET)

        resource_group_list = []
        _resource_group_list = d.pop("resourceGroupList", UNSET)
        for resource_group_list_item_data in _resource_group_list or []:
            resource_group_list_item = SSLVPNResourceBriefGroupEntity.from_dict(resource_group_list_item_data)

            resource_group_list.append(resource_group_list_item)

        ip = d.pop("ip", UNSET)

        mask = d.pop("mask", UNSET)

        domain = d.pop("domain", UNSET)

        protocol = d.pop("protocol", UNSET)

        src_port_start = d.pop("srcPortStart", UNSET)

        src_port_end = d.pop("srcPortEnd", UNSET)

        dst_port_start = d.pop("dstPortStart", UNSET)

        dst_port_end = d.pop("dstPortEnd", UNSET)

        icmp_type = d.pop("icmpType", UNSET)

        icmp_code = d.pop("icmpCode", UNSET)

        other_protocol = d.pop("otherProtocol", UNSET)

        sslvpn_resource_entity = cls(
            name=name,
            type=type,
            id=id,
            resource_group_list=resource_group_list,
            ip=ip,
            mask=mask,
            domain=domain,
            protocol=protocol,
            src_port_start=src_port_start,
            src_port_end=src_port_end,
            dst_port_start=dst_port_start,
            dst_port_end=dst_port_end,
            icmp_type=icmp_type,
            icmp_code=icmp_code,
            other_protocol=other_protocol,
        )

        sslvpn_resource_entity.additional_properties = d
        return sslvpn_resource_entity

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
