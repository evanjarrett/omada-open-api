from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drop_eap import DropEap
    from ..models.retry_eap import RetryEap


T = TypeVar("T", bound="RetryDropRate")


@_attrs_define
class RetryDropRate:
    """
    Attributes:
        retry_eaps (Union[Unset, List['RetryEap']]): AP list of retransmission packet rates tab, in descending order of
            average
        dropped_eaps (Union[Unset, List['DropEap']]): AP list of packet loss rate tab, in descending order of average
            value
    """

    retry_eaps: Union[Unset, List["RetryEap"]] = UNSET
    dropped_eaps: Union[Unset, List["DropEap"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        retry_eaps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.retry_eaps, Unset):
            retry_eaps = []
            for retry_eaps_item_data in self.retry_eaps:
                retry_eaps_item = retry_eaps_item_data.to_dict()

                retry_eaps.append(retry_eaps_item)

        dropped_eaps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dropped_eaps, Unset):
            dropped_eaps = []
            for dropped_eaps_item_data in self.dropped_eaps:
                dropped_eaps_item = dropped_eaps_item_data.to_dict()

                dropped_eaps.append(dropped_eaps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry_eaps is not UNSET:
            field_dict["retryEaps"] = retry_eaps
        if dropped_eaps is not UNSET:
            field_dict["droppedEaps"] = dropped_eaps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.drop_eap import DropEap
        from ..models.retry_eap import RetryEap

        d = src_dict.copy()
        retry_eaps = []
        _retry_eaps = d.pop("retryEaps", UNSET)
        for retry_eaps_item_data in _retry_eaps or []:
            retry_eaps_item = RetryEap.from_dict(retry_eaps_item_data)

            retry_eaps.append(retry_eaps_item)

        dropped_eaps = []
        _dropped_eaps = d.pop("droppedEaps", UNSET)
        for dropped_eaps_item_data in _dropped_eaps or []:
            dropped_eaps_item = DropEap.from_dict(dropped_eaps_item_data)

            dropped_eaps.append(dropped_eaps_item)

        retry_drop_rate = cls(
            retry_eaps=retry_eaps,
            dropped_eaps=dropped_eaps,
        )

        retry_drop_rate.additional_properties = d
        return retry_drop_rate

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
