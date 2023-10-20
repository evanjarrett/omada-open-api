from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollingUpgradeRequestInfo")


@_attrs_define
class RollingUpgradeRequestInfo:
    """
    Attributes:
        macs (Union[Unset, List[str]]): Mac list of devices
    """

    macs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        macs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        macs = cast(List[str], d.pop("macs", UNSET))

        rolling_upgrade_request_info = cls(
            macs=macs,
        )

        rolling_upgrade_request_info.additional_properties = d
        return rolling_upgrade_request_info

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
