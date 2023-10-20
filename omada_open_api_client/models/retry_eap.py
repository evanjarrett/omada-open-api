from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retry import Retry


T = TypeVar("T", bound="RetryEap")


@_attrs_define
class RetryEap:
    """AP list of retransmission packet rates tab, in descending order of average

    Attributes:
        retries (Union[Unset, List['Retry']]): AP retries timing list
        ap_mac (Union[Unset, str]): AP MAC
        name (Union[Unset, str]): AP name
        model (Union[Unset, str]): AP model
        model_version (Union[Unset, str]): AP model Version
        avg (Union[Unset, float]): Average current AP retransmission packet rate
        status (Union[Unset, int]): AP status
    """

    retries: Union[Unset, List["Retry"]] = UNSET
    ap_mac: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    model_version: Union[Unset, str] = UNSET
    avg: Union[Unset, float] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        retries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.retries, Unset):
            retries = []
            for retries_item_data in self.retries:
                retries_item = retries_item_data.to_dict()

                retries.append(retries_item)

        ap_mac = self.ap_mac
        name = self.name
        model = self.model
        model_version = self.model_version
        avg = self.avg
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retries is not UNSET:
            field_dict["retries"] = retries
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if avg is not UNSET:
            field_dict["avg"] = avg
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.retry import Retry

        d = src_dict.copy()
        retries = []
        _retries = d.pop("retries", UNSET)
        for retries_item_data in _retries or []:
            retries_item = Retry.from_dict(retries_item_data)

            retries.append(retries_item)

        ap_mac = d.pop("apMac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        avg = d.pop("avg", UNSET)

        status = d.pop("status", UNSET)

        retry_eap = cls(
            retries=retries,
            ap_mac=ap_mac,
            name=name,
            model=model,
            model_version=model_version,
            avg=avg,
            status=status,
        )

        retry_eap.additional_properties = d
        return retry_eap

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
