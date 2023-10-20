from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aplan_traffic_entity import APLANTrafficEntity


T = TypeVar("T", bound="APLANEntity")


@_attrs_define
class APLANEntity:
    """
    Attributes:
        lan_traffic (Union[Unset, APLANTrafficEntity]): LAN traffic info
    """

    lan_traffic: Union[Unset, "APLANTrafficEntity"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lan_traffic: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lan_traffic, Unset):
            lan_traffic = self.lan_traffic.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_traffic is not UNSET:
            field_dict["lanTraffic"] = lan_traffic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aplan_traffic_entity import APLANTrafficEntity

        d = src_dict.copy()
        _lan_traffic = d.pop("lanTraffic", UNSET)
        lan_traffic: Union[Unset, APLANTrafficEntity]
        if isinstance(_lan_traffic, Unset):
            lan_traffic = UNSET
        else:
            lan_traffic = APLANTrafficEntity.from_dict(_lan_traffic)

        aplan_entity = cls(
            lan_traffic=lan_traffic,
        )

        aplan_entity.additional_properties = d
        return aplan_entity

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
