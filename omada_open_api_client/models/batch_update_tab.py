from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateTab")


@_attrs_define
class BatchUpdateTab:
    """Edit Tab Parameters

    Attributes:
        id (Union[Unset, str]): which is a unique identifier
        cards (Union[Unset, List[int]]): Each number indicates a type of card. For details, see the description of the
            interface.
    """

    id: Union[Unset, str] = UNSET
    cards: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        cards: Union[Unset, List[int]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        cards = cast(List[int], d.pop("cards", UNSET))

        batch_update_tab = cls(
            id=id,
            cards=cards,
        )

        batch_update_tab.additional_properties = d
        return batch_update_tab

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
