from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_profile_entity import LanProfileEntity


T = TypeVar("T", bound="GridVOLanProfileEntity")


@_attrs_define
class GridVOLanProfileEntity:
    """
    Attributes:
        total_rows (Union[Unset, int]):
        current_page (Union[Unset, int]):
        current_size (Union[Unset, int]):
        data (Union[Unset, List['LanProfileEntity']]):
    """

    total_rows: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    current_size: Union[Unset, int] = UNSET
    data: Union[Unset, List["LanProfileEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_rows = self.total_rows
        current_page = self.current_page
        current_size = self.current_size
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lan_profile_entity import LanProfileEntity

        d = src_dict.copy()
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = LanProfileEntity.from_dict(data_item_data)

            data.append(data_item)

        grid_vo_lan_profile_entity = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
        )

        grid_vo_lan_profile_entity.additional_properties = d
        return grid_vo_lan_profile_entity

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
