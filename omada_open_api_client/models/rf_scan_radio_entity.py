from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interfernce_entity import InterfernceEntity


T = TypeVar("T", bound="RFScanRadioEntity")


@_attrs_define
class RFScanRadioEntity:
    """channel 6g

    Attributes:
        chan (Union[Unset, int]): channel number
        chan_width (Union[Unset, int]): range: {2, 3}, 2 means 20MHz, 3 means 40MHz, 5 means 80MHz
        util (Union[Unset, int]): channel utilization, range [0，100]
        inter (Union[Unset, List['InterfernceEntity']]): At most two types of interference data are reported in Inter,
            sorted in descending order of interference intensity
    """

    chan: Union[Unset, int] = UNSET
    chan_width: Union[Unset, int] = UNSET
    util: Union[Unset, int] = UNSET
    inter: Union[Unset, List["InterfernceEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chan = self.chan
        chan_width = self.chan_width
        util = self.util
        inter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inter, Unset):
            inter = []
            for inter_item_data in self.inter:
                inter_item = inter_item_data.to_dict()

                inter.append(inter_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chan is not UNSET:
            field_dict["chan"] = chan
        if chan_width is not UNSET:
            field_dict["chanWidth"] = chan_width
        if util is not UNSET:
            field_dict["util"] = util
        if inter is not UNSET:
            field_dict["inter"] = inter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interfernce_entity import InterfernceEntity

        d = src_dict.copy()
        chan = d.pop("chan", UNSET)

        chan_width = d.pop("chanWidth", UNSET)

        util = d.pop("util", UNSET)

        inter = []
        _inter = d.pop("inter", UNSET)
        for inter_item_data in _inter or []:
            inter_item = InterfernceEntity.from_dict(inter_item_data)

            inter.append(inter_item)

        rf_scan_radio_entity = cls(
            chan=chan,
            chan_width=chan_width,
            util=util,
            inter=inter,
        )

        rf_scan_radio_entity.additional_properties = d
        return rf_scan_radio_entity

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
