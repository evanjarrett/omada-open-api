from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormAuthCardAnswerOpenApiVO")


@_attrs_define
class FormAuthCardAnswerOpenApiVO:
    """Answers submitted by users

    Attributes:
        type (Union[Unset, int]): Type:

            0：single choice, 1：multiple choice,

            2：ComboBox, 3：input, 4：score, 5：prompt box
        choice_answer (Union[Unset, List[int]]): Drop-down menu or answer list for multiple-choice questions (exists if
            and only if cardType is 0, 1, 2)
        input_answer (Union[Unset, str]): Answers entered by the user, which corresponds to the question and answer
            question or the scored evaluation, or the input of other options in the multiple-choice question. Determined
            according to the type field. 0, 1, and 2 indicate other options answers, 3 indicates the answer in the input
            box, and 4 indicates the scored evaluation.
        score (Union[Unset, int]): User rating (range 1-5), exists when type is 4
        others (Union[Unset, str]): Exists when cardType is 0, 1 and the user adds other options. Used to save the
            option answer corresponding to the prompt of other options. Assuming that the user adds two other options, D and
            E, and choiceAnswer contains 3 ( D), 4 (E), then others[0] represents the answer of option D.
    """

    type: Union[Unset, int] = UNSET
    choice_answer: Union[Unset, List[int]] = UNSET
    input_answer: Union[Unset, str] = UNSET
    score: Union[Unset, int] = UNSET
    others: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        choice_answer: Union[Unset, List[int]] = UNSET
        if not isinstance(self.choice_answer, Unset):
            choice_answer = self.choice_answer

        input_answer = self.input_answer
        score = self.score
        others = self.others

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if choice_answer is not UNSET:
            field_dict["choiceAnswer"] = choice_answer
        if input_answer is not UNSET:
            field_dict["inputAnswer"] = input_answer
        if score is not UNSET:
            field_dict["score"] = score
        if others is not UNSET:
            field_dict["others"] = others

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        choice_answer = cast(List[int], d.pop("choiceAnswer", UNSET))

        input_answer = d.pop("inputAnswer", UNSET)

        score = d.pop("score", UNSET)

        others = d.pop("others", UNSET)

        form_auth_card_answer_open_api_vo = cls(
            type=type,
            choice_answer=choice_answer,
            input_answer=input_answer,
            score=score,
            others=others,
        )

        form_auth_card_answer_open_api_vo.additional_properties = d
        return form_auth_card_answer_open_api_vo

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
