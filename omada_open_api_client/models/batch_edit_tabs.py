from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_update_tab import BatchUpdateTab


T = TypeVar("T", bound="BatchEditTabs")


@_attrs_define
class BatchEditTabs:
    """
    Attributes:
        tabs (Union[Unset, List['BatchUpdateTab']]): Edit Tab Parameters
    """

    tabs: Union[Unset, List["BatchUpdateTab"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tabs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tabs, Unset):
            tabs = []
            for tabs_item_data in self.tabs:
                tabs_item = tabs_item_data.to_dict()

                tabs.append(tabs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tabs is not UNSET:
            field_dict["tabs"] = tabs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_update_tab import BatchUpdateTab

        d = src_dict.copy()
        tabs = []
        _tabs = d.pop("tabs", UNSET)
        for tabs_item_data in _tabs or []:
            tabs_item = BatchUpdateTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        batch_edit_tabs = cls(
            tabs=tabs,
        )

        batch_edit_tabs.additional_properties = d
        return batch_edit_tabs

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
