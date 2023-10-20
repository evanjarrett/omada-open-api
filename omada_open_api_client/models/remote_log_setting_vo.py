from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteLogSettingVO")


@_attrs_define
class RemoteLogSettingVO:
    """
    Attributes:
        enable (bool):
        host (Union[Unset, str]):
        port (Union[Unset, int]):
        more_client_log (Union[Unset, bool]):
    """

    enable: bool
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    more_client_log: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        host = self.host
        port = self.port
        more_client_log = self.more_client_log

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if more_client_log is not UNSET:
            field_dict["moreClientLog"] = more_client_log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        more_client_log = d.pop("moreClientLog", UNSET)

        remote_log_setting_vo = cls(
            enable=enable,
            host=host,
            port=port,
            more_client_log=more_client_log,
        )

        remote_log_setting_vo.additional_properties = d
        return remote_log_setting_vo

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
