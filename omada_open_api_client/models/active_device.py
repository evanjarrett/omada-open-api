from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveDevice")


@_attrs_define
class ActiveDevice:
    """
    Attributes:
        status (Union[Unset, int]): There are two types of status: Connected, and Disconnected. 0 means Connected. 1
            means Disconnected.
        name (Union[Unset, str]): Device name
        traffic (Union[Unset, float]): Traffic measured in GB
        mac (Union[Unset, str]): Device MAC address, linked to the device details page
        model (Union[Unset, str]): Device model, such as : EAP620 HD
        model_version (Union[Unset, str]): Model version, such as : 3.0
    """

    status: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    traffic: Union[Unset, float] = UNSET
    mac: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    model_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        name = self.name
        traffic = self.traffic
        mac = self.mac
        model = self.model
        model_version = self.model_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        name = d.pop("name", UNSET)

        traffic = d.pop("traffic", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        active_device = cls(
            status=status,
            name=name,
            traffic=traffic,
            mac=mac,
            model=model,
            model_version=model_version,
        )

        active_device.additional_properties = d
        return active_device

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
