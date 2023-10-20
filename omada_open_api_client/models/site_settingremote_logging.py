from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_log_setting_vo import RemoteLogSettingVO


T = TypeVar("T", bound="SiteSettingremoteLogging")


@_attrs_define
class SiteSettingremoteLogging:
    """
    Attributes:
        remote_log (Union[Unset, RemoteLogSettingVO]):
    """

    remote_log: Union[Unset, "RemoteLogSettingVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remote_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remote_log, Unset):
            remote_log = self.remote_log.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_log is not UNSET:
            field_dict["remoteLog"] = remote_log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remote_log_setting_vo import RemoteLogSettingVO

        d = src_dict.copy()
        _remote_log = d.pop("remoteLog", UNSET)
        remote_log: Union[Unset, RemoteLogSettingVO]
        if isinstance(_remote_log, Unset):
            remote_log = UNSET
        else:
            remote_log = RemoteLogSettingVO.from_dict(_remote_log)

        site_settingremote_logging = cls(
            remote_log=remote_log,
        )

        site_settingremote_logging.additional_properties = d
        return site_settingremote_logging

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
