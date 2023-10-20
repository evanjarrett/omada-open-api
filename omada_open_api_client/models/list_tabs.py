from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTabs")


@_attrs_define
class ListTabs:
    """
    Attributes:
        id (Union[Unset, str]): A unique identifier
        name (Union[Unset, str]): Name cannot be duplicated on the dashboard page
        type (Union[Unset, int]): There are three types of tab: Network, Clients, and Customized.1 means Network.2 means
            Clients.3 means Customized.
        cards (Union[Unset, List[int]]): Card list displayed in Tab. Each number indicates a type of card. such as 101:
            Alerts
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    cards: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type
        cards: Union[Unset, List[int]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        cards = cast(List[int], d.pop("cards", UNSET))

        list_tabs = cls(
            id=id,
            name=name,
            type=type,
            cards=cards,
        )

        list_tabs.additional_properties = d
        return list_tabs

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
