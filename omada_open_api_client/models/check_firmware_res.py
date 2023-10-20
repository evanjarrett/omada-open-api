from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckFirmwareRes")


@_attrs_define
class CheckFirmwareRes:
    """
    Attributes:
        finished (Union[Unset, bool]): Whether the task is complete
        ap_mac_list (Union[Unset, List[str]]): List of the ap mac address with firmware updates
        switch_mac_list (Union[Unset, List[str]]): List of switch mac address with firmware updates
        gateway_mac_list (Union[Unset, List[str]]): List of gateway mac address with firmware updates
    """

    finished: Union[Unset, bool] = UNSET
    ap_mac_list: Union[Unset, List[str]] = UNSET
    switch_mac_list: Union[Unset, List[str]] = UNSET
    gateway_mac_list: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finished = self.finished
        ap_mac_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ap_mac_list, Unset):
            ap_mac_list = self.ap_mac_list

        switch_mac_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.switch_mac_list, Unset):
            switch_mac_list = self.switch_mac_list

        gateway_mac_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.gateway_mac_list, Unset):
            gateway_mac_list = self.gateway_mac_list

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished is not UNSET:
            field_dict["finished"] = finished
        if ap_mac_list is not UNSET:
            field_dict["apMacList"] = ap_mac_list
        if switch_mac_list is not UNSET:
            field_dict["switchMacList"] = switch_mac_list
        if gateway_mac_list is not UNSET:
            field_dict["gatewayMacList"] = gateway_mac_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        finished = d.pop("finished", UNSET)

        ap_mac_list = cast(List[str], d.pop("apMacList", UNSET))

        switch_mac_list = cast(List[str], d.pop("switchMacList", UNSET))

        gateway_mac_list = cast(List[str], d.pop("gatewayMacList", UNSET))

        check_firmware_res = cls(
            finished=finished,
            ap_mac_list=ap_mac_list,
            switch_mac_list=switch_mac_list,
            gateway_mac_list=gateway_mac_list,
        )

        check_firmware_res.additional_properties = d
        return check_firmware_res

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
