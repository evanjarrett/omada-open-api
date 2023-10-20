from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_interference import ApInterference


T = TypeVar("T", bound="ApInterferences")


@_attrs_define
class ApInterferences:
    """
    Attributes:
        ap_interference_2_g (Union[Unset, List['ApInterference']]): 2GHz device interference intensity information
        ap_interference_5_g (Union[Unset, List['ApInterference']]): 5GHz device interference intensity information
        ap_interference_5_g_2 (Union[Unset, List['ApInterference']]): 5GHz-2 device interference intensity information
        ap_interference_6_g (Union[Unset, List['ApInterference']]): 6GHz device interference intensity information
    """

    ap_interference_2_g: Union[Unset, List["ApInterference"]] = UNSET
    ap_interference_5_g: Union[Unset, List["ApInterference"]] = UNSET
    ap_interference_5_g_2: Union[Unset, List["ApInterference"]] = UNSET
    ap_interference_6_g: Union[Unset, List["ApInterference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ap_interference_2_g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ap_interference_2_g, Unset):
            ap_interference_2_g = []
            for ap_interference_2_g_item_data in self.ap_interference_2_g:
                ap_interference_2_g_item = ap_interference_2_g_item_data.to_dict()

                ap_interference_2_g.append(ap_interference_2_g_item)

        ap_interference_5_g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ap_interference_5_g, Unset):
            ap_interference_5_g = []
            for ap_interference_5_g_item_data in self.ap_interference_5_g:
                ap_interference_5_g_item = ap_interference_5_g_item_data.to_dict()

                ap_interference_5_g.append(ap_interference_5_g_item)

        ap_interference_5_g_2: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ap_interference_5_g_2, Unset):
            ap_interference_5_g_2 = []
            for ap_interference_5_g_2_item_data in self.ap_interference_5_g_2:
                ap_interference_5_g_2_item = ap_interference_5_g_2_item_data.to_dict()

                ap_interference_5_g_2.append(ap_interference_5_g_2_item)

        ap_interference_6_g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ap_interference_6_g, Unset):
            ap_interference_6_g = []
            for ap_interference_6_g_item_data in self.ap_interference_6_g:
                ap_interference_6_g_item = ap_interference_6_g_item_data.to_dict()

                ap_interference_6_g.append(ap_interference_6_g_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_interference_2_g is not UNSET:
            field_dict["apInterference2g"] = ap_interference_2_g
        if ap_interference_5_g is not UNSET:
            field_dict["apInterference5g"] = ap_interference_5_g
        if ap_interference_5_g_2 is not UNSET:
            field_dict["apInterference5g2"] = ap_interference_5_g_2
        if ap_interference_6_g is not UNSET:
            field_dict["apInterference6g"] = ap_interference_6_g

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_interference import ApInterference

        d = src_dict.copy()
        ap_interference_2_g = []
        _ap_interference_2_g = d.pop("apInterference2g", UNSET)
        for ap_interference_2_g_item_data in _ap_interference_2_g or []:
            ap_interference_2_g_item = ApInterference.from_dict(ap_interference_2_g_item_data)

            ap_interference_2_g.append(ap_interference_2_g_item)

        ap_interference_5_g = []
        _ap_interference_5_g = d.pop("apInterference5g", UNSET)
        for ap_interference_5_g_item_data in _ap_interference_5_g or []:
            ap_interference_5_g_item = ApInterference.from_dict(ap_interference_5_g_item_data)

            ap_interference_5_g.append(ap_interference_5_g_item)

        ap_interference_5_g_2 = []
        _ap_interference_5_g_2 = d.pop("apInterference5g2", UNSET)
        for ap_interference_5_g_2_item_data in _ap_interference_5_g_2 or []:
            ap_interference_5_g_2_item = ApInterference.from_dict(ap_interference_5_g_2_item_data)

            ap_interference_5_g_2.append(ap_interference_5_g_2_item)

        ap_interference_6_g = []
        _ap_interference_6_g = d.pop("apInterference6g", UNSET)
        for ap_interference_6_g_item_data in _ap_interference_6_g or []:
            ap_interference_6_g_item = ApInterference.from_dict(ap_interference_6_g_item_data)

            ap_interference_6_g.append(ap_interference_6_g_item)

        ap_interferences = cls(
            ap_interference_2_g=ap_interference_2_g,
            ap_interference_5_g=ap_interference_5_g,
            ap_interference_5_g_2=ap_interference_5_g_2,
            ap_interference_6_g=ap_interference_6_g,
        )

        ap_interferences.additional_properties = d
        return ap_interferences

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
