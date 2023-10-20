from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_brief_info_vo import ApBriefInfoVO


T = TypeVar("T", bound="ClientLockToApSetting")


@_attrs_define
class ClientLockToApSetting:
    """Client lock to ap setting

    Attributes:
        enable (Union[Unset, bool]): Lock to ap enable
        aps (Union[Unset, List['ApBriefInfoVO']]): Ap name and mac info list
    """

    enable: Union[Unset, bool] = UNSET
    aps: Union[Unset, List["ApBriefInfoVO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        aps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aps, Unset):
            aps = []
            for aps_item_data in self.aps:
                aps_item = aps_item_data.to_dict()

                aps.append(aps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if aps is not UNSET:
            field_dict["aps"] = aps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_brief_info_vo import ApBriefInfoVO

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        aps = []
        _aps = d.pop("aps", UNSET)
        for aps_item_data in _aps or []:
            aps_item = ApBriefInfoVO.from_dict(aps_item_data)

            aps.append(aps_item)

        client_lock_to_ap_setting = cls(
            enable=enable,
            aps=aps,
        )

        client_lock_to_ap_setting.additional_properties = d
        return client_lock_to_ap_setting

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
