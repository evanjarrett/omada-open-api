from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceFirmwareInfo")


@_attrs_define
class DeviceFirmwareInfo:
    """
    Attributes:
        cur_fw_ver (Union[Unset, str]): Current firmware version
        last_fw_ver (Union[Unset, str]): Latest firmware version
        fw_release_log (Union[Unset, str]): Firmware release log
    """

    cur_fw_ver: Union[Unset, str] = UNSET
    last_fw_ver: Union[Unset, str] = UNSET
    fw_release_log: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cur_fw_ver = self.cur_fw_ver
        last_fw_ver = self.last_fw_ver
        fw_release_log = self.fw_release_log

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_fw_ver is not UNSET:
            field_dict["curFwVer"] = cur_fw_ver
        if last_fw_ver is not UNSET:
            field_dict["lastFwVer"] = last_fw_ver
        if fw_release_log is not UNSET:
            field_dict["fwReleaseLog"] = fw_release_log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cur_fw_ver = d.pop("curFwVer", UNSET)

        last_fw_ver = d.pop("lastFwVer", UNSET)

        fw_release_log = d.pop("fwReleaseLog", UNSET)

        device_firmware_info = cls(
            cur_fw_ver=cur_fw_ver,
            last_fw_ver=last_fw_ver,
            fw_release_log=fw_release_log,
        )

        device_firmware_info.additional_properties = d
        return device_firmware_info

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
