from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_ap_lldp_setting_vo import SiteApLldpSettingVO


T = TypeVar("T", bound="SiteSettinglldp")


@_attrs_define
class SiteSettinglldp:
    """
    Attributes:
        lldp (Union[Unset, SiteApLldpSettingVO]):
    """

    lldp: Union[Unset, "SiteApLldpSettingVO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lldp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lldp, Unset):
            lldp = self.lldp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lldp is not UNSET:
            field_dict["lldp"] = lldp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_ap_lldp_setting_vo import SiteApLldpSettingVO

        d = src_dict.copy()
        _lldp = d.pop("lldp", UNSET)
        lldp: Union[Unset, SiteApLldpSettingVO]
        if isinstance(_lldp, Unset):
            lldp = UNSET
        else:
            lldp = SiteApLldpSettingVO.from_dict(_lldp)

        site_settinglldp = cls(
            lldp=lldp,
        )

        site_settinglldp.additional_properties = d
        return site_settinglldp

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
