from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdoptDeviceResultInfo")


@_attrs_define
class AdoptDeviceResultInfo:
    """
    Attributes:
        device_mac (Union[Unset, str]): Device mac
        adopt_error_code (Union[Unset, int]): Adopt result.0:Adopt Device Success.-39002:Device adoption failed because
            the device does not respond to adopt commands.-39003:Failed to adopt the Device. The username or password  is
            incorrect.-39004:Failed to adopt device.-39005:Failed to adopt this device because the device is not
            connected.-39329:Failed to link to the uplink AP.
        adopt_failed_type (Union[Unset, int]): Adopt failed type.-1:No need print username or password.-2:Need print
            username or password.
    """

    device_mac: Union[Unset, str] = UNSET
    adopt_error_code: Union[Unset, int] = UNSET
    adopt_failed_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_mac = self.device_mac
        adopt_error_code = self.adopt_error_code
        adopt_failed_type = self.adopt_failed_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if adopt_error_code is not UNSET:
            field_dict["adoptErrorCode"] = adopt_error_code
        if adopt_failed_type is not UNSET:
            field_dict["adoptFailedType"] = adopt_failed_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_mac = d.pop("deviceMac", UNSET)

        adopt_error_code = d.pop("adoptErrorCode", UNSET)

        adopt_failed_type = d.pop("adoptFailedType", UNSET)

        adopt_device_result_info = cls(
            device_mac=device_mac,
            adopt_error_code=adopt_error_code,
            adopt_failed_type=adopt_failed_type,
        )

        adopt_device_result_info.additional_properties = d
        return adopt_device_result_info

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
