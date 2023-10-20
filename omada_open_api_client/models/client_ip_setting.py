from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientIpSetting")


@_attrs_define
class ClientIpSetting:
    """
    Attributes:
        use_fixed_addr (bool): Whether to use the specified IP
        net_id (Union[Unset, str]): Lan network id
        ip (Union[Unset, str]): Client IP
    """

    use_fixed_addr: bool
    net_id: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_fixed_addr = self.use_fixed_addr
        net_id = self.net_id
        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useFixedAddr": use_fixed_addr,
            }
        )
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_fixed_addr = d.pop("useFixedAddr")

        net_id = d.pop("netId", UNSET)

        ip = d.pop("ip", UNSET)

        client_ip_setting = cls(
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            ip=ip,
        )

        client_ip_setting.additional_properties = d
        return client_ip_setting

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
