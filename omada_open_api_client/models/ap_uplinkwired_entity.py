from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_wired_uplink_entity import APWiredUplinkEntity


T = TypeVar("T", bound="APUplinkwiredEntity")


@_attrs_define
class APUplinkwiredEntity:
    """
    Attributes:
        wired_uplink (Union[Unset, APWiredUplinkEntity]): wired uplink info
    """

    wired_uplink: Union[Unset, "APWiredUplinkEntity"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wired_uplink: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wired_uplink, Unset):
            wired_uplink = self.wired_uplink.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wired_uplink is not UNSET:
            field_dict["wiredUplink"] = wired_uplink

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_wired_uplink_entity import APWiredUplinkEntity

        d = src_dict.copy()
        _wired_uplink = d.pop("wiredUplink", UNSET)
        wired_uplink: Union[Unset, APWiredUplinkEntity]
        if isinstance(_wired_uplink, Unset):
            wired_uplink = UNSET
        else:
            wired_uplink = APWiredUplinkEntity.from_dict(_wired_uplink)

        ap_uplinkwired_entity = cls(
            wired_uplink=wired_uplink,
        )

        ap_uplinkwired_entity.additional_properties = d
        return ap_uplinkwired_entity

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
