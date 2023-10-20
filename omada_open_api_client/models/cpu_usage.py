from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CpuUsage")


@_attrs_define
class CpuUsage:
    """
    Attributes:
        name (Union[Unset, str]): Device name
        mac (Union[Unset, str]): Device MAC
        cpu_util (Union[Unset, int]): Device CPU utilization
        model (Union[Unset, str]): Device model
        model_version (Union[Unset, str]): Device model version
        type (Union[Unset, str]): Device type
    """

    name: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    cpu_util: Union[Unset, int] = UNSET
    model: Union[Unset, str] = UNSET
    model_version: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        mac = self.mac
        cpu_util = self.cpu_util
        model = self.model
        model_version = self.model_version
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type = d.pop("type", UNSET)

        cpu_usage = cls(
            name=name,
            mac=mac,
            cpu_util=cpu_util,
            model=model,
            model_version=model_version,
            type=type,
        )

        cpu_usage.additional_properties = d
        return cpu_usage

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
