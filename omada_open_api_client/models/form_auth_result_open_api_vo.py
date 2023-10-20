from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_auth_card_answer_open_api_vo import FormAuthCardAnswerOpenApiVO


T = TypeVar("T", bound="FormAuthResultOpenApiVO")


@_attrs_define
class FormAuthResultOpenApiVO:
    """
    Attributes:
        id (Union[Unset, str]): id
        form_id (Union[Unset, str]): form id
        answers (Union[Unset, List['FormAuthCardAnswerOpenApiVO']]): Answers submitted by users
        time (Union[Unset, int]): Authenticated timestamp in ms.
        ssid (Union[Unset, str]): Client connected SSID
        network (Union[Unset, str]): Network (exists when wired connection)
    """

    id: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    answers: Union[Unset, List["FormAuthCardAnswerOpenApiVO"]] = UNSET
    time: Union[Unset, int] = UNSET
    ssid: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        form_id = self.form_id
        answers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()

                answers.append(answers_item)

        time = self.time
        ssid = self.ssid
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if answers is not UNSET:
            field_dict["answers"] = answers
        if time is not UNSET:
            field_dict["time"] = time
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_auth_card_answer_open_api_vo import FormAuthCardAnswerOpenApiVO

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        form_id = d.pop("formId", UNSET)

        answers = []
        _answers = d.pop("answers", UNSET)
        for answers_item_data in _answers or []:
            answers_item = FormAuthCardAnswerOpenApiVO.from_dict(answers_item_data)

            answers.append(answers_item)

        time = d.pop("time", UNSET)

        ssid = d.pop("ssid", UNSET)

        network = d.pop("network", UNSET)

        form_auth_result_open_api_vo = cls(
            id=id,
            form_id=form_id,
            answers=answers,
            time=time,
            ssid=ssid,
            network=network,
        )

        form_auth_result_open_api_vo.additional_properties = d
        return form_auth_result_open_api_vo

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
