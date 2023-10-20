from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_time_entity import AuthTimeEntity
    from ..models.form_auth_card_entity import FormAuthCardEntity


T = TypeVar("T", bound="FormAuthOpenApiVO")


@_attrs_define
class FormAuthOpenApiVO:
    """
    Attributes:
        id (Union[Unset, str]): auth form id
        title (Union[Unset, str]): Form title (display for the authentication user).Length of title is from 1 to 2000.
        name (Union[Unset, str]): Form name (display for the controller user).Length of title is from 1 to 2000.
        note (Union[Unset, str]): Note. Length of title is from 1 to 2000.
        auth_timeout (Union[Unset, AuthTimeEntity]): Authentication timeout time. Display when enabled, otherwise no
            display.
        card_list (Union[Unset, List['FormAuthCardEntity']]): Form card list.
        is_published (Union[Unset, bool]): Whether to publish.
        create_time (Union[Unset, int]): Created time of the form.
        portals (Union[Unset, List[str]]): Portal names corresponding to the bound portal.
        answer_num (Union[Unset, int]): The number of form's answers.
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    auth_timeout: Union[Unset, "AuthTimeEntity"] = UNSET
    card_list: Union[Unset, List["FormAuthCardEntity"]] = UNSET
    is_published: Union[Unset, bool] = UNSET
    create_time: Union[Unset, int] = UNSET
    portals: Union[Unset, List[str]] = UNSET
    answer_num: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        name = self.name
        note = self.note
        auth_timeout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_timeout, Unset):
            auth_timeout = self.auth_timeout.to_dict()

        card_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.card_list, Unset):
            card_list = []
            for card_list_item_data in self.card_list:
                card_list_item = card_list_item_data.to_dict()

                card_list.append(card_list_item)

        is_published = self.is_published
        create_time = self.create_time
        portals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.portals, Unset):
            portals = self.portals

        answer_num = self.answer_num

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if auth_timeout is not UNSET:
            field_dict["authTimeout"] = auth_timeout
        if card_list is not UNSET:
            field_dict["cardList"] = card_list
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if portals is not UNSET:
            field_dict["portals"] = portals
        if answer_num is not UNSET:
            field_dict["answerNum"] = answer_num

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auth_time_entity import AuthTimeEntity
        from ..models.form_auth_card_entity import FormAuthCardEntity

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        name = d.pop("name", UNSET)

        note = d.pop("note", UNSET)

        _auth_timeout = d.pop("authTimeout", UNSET)
        auth_timeout: Union[Unset, AuthTimeEntity]
        if isinstance(_auth_timeout, Unset):
            auth_timeout = UNSET
        else:
            auth_timeout = AuthTimeEntity.from_dict(_auth_timeout)

        card_list = []
        _card_list = d.pop("cardList", UNSET)
        for card_list_item_data in _card_list or []:
            card_list_item = FormAuthCardEntity.from_dict(card_list_item_data)

            card_list.append(card_list_item)

        is_published = d.pop("isPublished", UNSET)

        create_time = d.pop("createTime", UNSET)

        portals = cast(List[str], d.pop("portals", UNSET))

        answer_num = d.pop("answerNum", UNSET)

        form_auth_open_api_vo = cls(
            id=id,
            title=title,
            name=name,
            note=note,
            auth_timeout=auth_timeout,
            card_list=card_list,
            is_published=is_published,
            create_time=create_time,
            portals=portals,
            answer_num=answer_num,
        )

        form_auth_open_api_vo.additional_properties = d
        return form_auth_open_api_vo

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
