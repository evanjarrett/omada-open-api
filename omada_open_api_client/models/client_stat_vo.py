from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientStatVO")


@_attrs_define
class ClientStatVO:
    """
    Attributes:
        total (Union[Unset, int]):
        wireless (Union[Unset, int]):
        wired (Union[Unset, int]):
        num2g (Union[Unset, int]):
        num5g (Union[Unset, int]):
        num6g (Union[Unset, int]):
        num_user (Union[Unset, int]):
        num_guest (Union[Unset, int]):
        num_wireless_user (Union[Unset, int]):
        num_wireless_guest (Union[Unset, int]):
        num_2_g_user (Union[Unset, int]):
        num_5_g_user (Union[Unset, int]):
        num_6_g_user (Union[Unset, int]):
        num_2_g_guest (Union[Unset, int]):
        num_5_g_guest (Union[Unset, int]):
        num_6_g_guest (Union[Unset, int]):
        poor (Union[Unset, int]):
        fair (Union[Unset, int]):
        no_data (Union[Unset, int]):
        good (Union[Unset, int]):
    """

    total: Union[Unset, int] = UNSET
    wireless: Union[Unset, int] = UNSET
    wired: Union[Unset, int] = UNSET
    num2g: Union[Unset, int] = UNSET
    num5g: Union[Unset, int] = UNSET
    num6g: Union[Unset, int] = UNSET
    num_user: Union[Unset, int] = UNSET
    num_guest: Union[Unset, int] = UNSET
    num_wireless_user: Union[Unset, int] = UNSET
    num_wireless_guest: Union[Unset, int] = UNSET
    num_2_g_user: Union[Unset, int] = UNSET
    num_5_g_user: Union[Unset, int] = UNSET
    num_6_g_user: Union[Unset, int] = UNSET
    num_2_g_guest: Union[Unset, int] = UNSET
    num_5_g_guest: Union[Unset, int] = UNSET
    num_6_g_guest: Union[Unset, int] = UNSET
    poor: Union[Unset, int] = UNSET
    fair: Union[Unset, int] = UNSET
    no_data: Union[Unset, int] = UNSET
    good: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        wireless = self.wireless
        wired = self.wired
        num2g = self.num2g
        num5g = self.num5g
        num6g = self.num6g
        num_user = self.num_user
        num_guest = self.num_guest
        num_wireless_user = self.num_wireless_user
        num_wireless_guest = self.num_wireless_guest
        num_2_g_user = self.num_2_g_user
        num_5_g_user = self.num_5_g_user
        num_6_g_user = self.num_6_g_user
        num_2_g_guest = self.num_2_g_guest
        num_5_g_guest = self.num_5_g_guest
        num_6_g_guest = self.num_6_g_guest
        poor = self.poor
        fair = self.fair
        no_data = self.no_data
        good = self.good

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if wired is not UNSET:
            field_dict["wired"] = wired
        if num2g is not UNSET:
            field_dict["num2g"] = num2g
        if num5g is not UNSET:
            field_dict["num5g"] = num5g
        if num6g is not UNSET:
            field_dict["num6g"] = num6g
        if num_user is not UNSET:
            field_dict["numUser"] = num_user
        if num_guest is not UNSET:
            field_dict["numGuest"] = num_guest
        if num_wireless_user is not UNSET:
            field_dict["numWirelessUser"] = num_wireless_user
        if num_wireless_guest is not UNSET:
            field_dict["numWirelessGuest"] = num_wireless_guest
        if num_2_g_user is not UNSET:
            field_dict["num2gUser"] = num_2_g_user
        if num_5_g_user is not UNSET:
            field_dict["num5gUser"] = num_5_g_user
        if num_6_g_user is not UNSET:
            field_dict["num6gUser"] = num_6_g_user
        if num_2_g_guest is not UNSET:
            field_dict["num2gGuest"] = num_2_g_guest
        if num_5_g_guest is not UNSET:
            field_dict["num5gGuest"] = num_5_g_guest
        if num_6_g_guest is not UNSET:
            field_dict["num6gGuest"] = num_6_g_guest
        if poor is not UNSET:
            field_dict["poor"] = poor
        if fair is not UNSET:
            field_dict["fair"] = fair
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if good is not UNSET:
            field_dict["good"] = good

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        wireless = d.pop("wireless", UNSET)

        wired = d.pop("wired", UNSET)

        num2g = d.pop("num2g", UNSET)

        num5g = d.pop("num5g", UNSET)

        num6g = d.pop("num6g", UNSET)

        num_user = d.pop("numUser", UNSET)

        num_guest = d.pop("numGuest", UNSET)

        num_wireless_user = d.pop("numWirelessUser", UNSET)

        num_wireless_guest = d.pop("numWirelessGuest", UNSET)

        num_2_g_user = d.pop("num2gUser", UNSET)

        num_5_g_user = d.pop("num5gUser", UNSET)

        num_6_g_user = d.pop("num6gUser", UNSET)

        num_2_g_guest = d.pop("num2gGuest", UNSET)

        num_5_g_guest = d.pop("num5gGuest", UNSET)

        num_6_g_guest = d.pop("num6gGuest", UNSET)

        poor = d.pop("poor", UNSET)

        fair = d.pop("fair", UNSET)

        no_data = d.pop("noData", UNSET)

        good = d.pop("good", UNSET)

        client_stat_vo = cls(
            total=total,
            wireless=wireless,
            wired=wired,
            num2g=num2g,
            num5g=num5g,
            num6g=num6g,
            num_user=num_user,
            num_guest=num_guest,
            num_wireless_user=num_wireless_user,
            num_wireless_guest=num_wireless_guest,
            num_2_g_user=num_2_g_user,
            num_5_g_user=num_5_g_user,
            num_6_g_user=num_6_g_user,
            num_2_g_guest=num_2_g_guest,
            num_5_g_guest=num_5_g_guest,
            num_6_g_guest=num_6_g_guest,
            poor=poor,
            fair=fair,
            no_data=no_data,
            good=good,
        )

        client_stat_vo.additional_properties = d
        return client_stat_vo

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
