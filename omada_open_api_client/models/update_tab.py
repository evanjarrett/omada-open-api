from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTab")


@_attrs_define
class UpdateTab:
    """
    Attributes:
        name (Union[Unset, str]): Names on this Dashboard page must be unique.
        cards (Union[Unset, List[int]]): Card list displayed in Tab. Each number indicates a type of card. Such as 101:
            Alerts.
        reset (Union[Unset, bool]): True: reset Default TAB (custom TAB cannot be reset).
    """

    name: Union[Unset, str] = UNSET
    cards: Union[Unset, List[int]] = UNSET
    reset: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        cards: Union[Unset, List[int]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        reset = self.reset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if cards is not UNSET:
            field_dict["cards"] = cards
        if reset is not UNSET:
            field_dict["reset"] = reset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        cards = cast(List[int], d.pop("cards", UNSET))

        reset = d.pop("reset", UNSET)

        update_tab = cls(
            name=name,
            cards=cards,
            reset=reset,
        )

        update_tab.additional_properties = d
        return update_tab

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
