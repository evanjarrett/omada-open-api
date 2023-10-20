from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormAuthCardEntity")


@_attrs_define
class FormAuthCardEntity:
    """Form card list.

    Attributes:
        type (int): Card type list (0: single choice (single choice), 1: multiple choice (multiple choice), 2: ComboBox
            (drop-down menu), 3: input (input box), 4: score (score), 5: prompt frame
        required (bool): Indicates whether the card is required (cardType is 5, meaningless in the prompt box).
        title (str): Title.Length of title is from 1 to 2000.
        choices (List[str]): Drop-down menu or list of options for multiple-choice questions (exist if and only if
            cardType is 0, 1, 2), excluding questions with other options.
        score_notes (List[str]): The prompt text corresponding to different scores of the scoring card. Exists when the
            cardType is 4 and needs to be transmitted in order. The subscript 0 corresponds to the score 1.
        others (Union[Unset, str]): The question of the other options. Exists if and only if type is 0, 1.
    """

    type: int
    required: bool
    title: str
    choices: List[str]
    score_notes: List[str]
    others: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        required = self.required
        title = self.title
        choices = self.choices

        score_notes = self.score_notes

        others = self.others

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "required": required,
                "title": title,
                "choices": choices,
                "scoreNotes": score_notes,
            }
        )
        if others is not UNSET:
            field_dict["others"] = others

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        required = d.pop("required")

        title = d.pop("title")

        choices = cast(List[str], d.pop("choices"))

        score_notes = cast(List[str], d.pop("scoreNotes"))

        others = d.pop("others", UNSET)

        form_auth_card_entity = cls(
            type=type,
            required=required,
            title=title,
            choices=choices,
            score_notes=score_notes,
            others=others,
        )

        form_auth_card_entity.additional_properties = d
        return form_auth_card_entity

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
