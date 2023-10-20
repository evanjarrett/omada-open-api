from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auth_time_entity import AuthTimeEntity
    from ..models.form_auth_card_entity import FormAuthCardEntity


T = TypeVar("T", bound="FormAuthEntity")


@_attrs_define
class FormAuthEntity:
    """
    Attributes:
        title (str): Form title (display for the authentication user).Length of title is from 1 to 2000.
        name (str): Form name (display for the controller user).Length of title is from 1 to 2000.
        note (str): Note. Length of note is from 1 to 2000.
        auth_timeout (AuthTimeEntity): Authentication timeout time. Display when enabled, otherwise no display.
        card_list (List['FormAuthCardEntity']): Form card list.
        published (bool): Whether to publish.
    """

    title: str
    name: str
    note: str
    auth_timeout: "AuthTimeEntity"
    card_list: List["FormAuthCardEntity"]
    published: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        name = self.name
        note = self.note
        auth_timeout = self.auth_timeout.to_dict()

        card_list = []
        for card_list_item_data in self.card_list:
            card_list_item = card_list_item_data.to_dict()

            card_list.append(card_list_item)

        published = self.published

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "name": name,
                "note": note,
                "authTimeout": auth_timeout,
                "cardList": card_list,
                "published": published,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auth_time_entity import AuthTimeEntity
        from ..models.form_auth_card_entity import FormAuthCardEntity

        d = src_dict.copy()
        title = d.pop("title")

        name = d.pop("name")

        note = d.pop("note")

        auth_timeout = AuthTimeEntity.from_dict(d.pop("authTimeout"))

        card_list = []
        _card_list = d.pop("cardList")
        for card_list_item_data in _card_list:
            card_list_item = FormAuthCardEntity.from_dict(card_list_item_data)

            card_list.append(card_list_item)

        published = d.pop("published")

        form_auth_entity = cls(
            title=title,
            name=name,
            note=note,
            auth_timeout=auth_timeout,
            card_list=card_list,
            published=published,
        )

        form_auth_entity.additional_properties = d
        return form_auth_entity

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
