from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollingUpgradeRes")


@_attrs_define
class RollingUpgradeRes:
    """
    Attributes:
        finished (Union[Unset, bool]): Whether the task is complete
        unfinished_count (Union[Unset, int]): Total number of devices that have not been upgraded
    """

    finished: Union[Unset, bool] = UNSET
    unfinished_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finished = self.finished
        unfinished_count = self.unfinished_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished is not UNSET:
            field_dict["finished"] = finished
        if unfinished_count is not UNSET:
            field_dict["unfinishedCount"] = unfinished_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        finished = d.pop("finished", UNSET)

        unfinished_count = d.pop("unfinishedCount", UNSET)

        rolling_upgrade_res = cls(
            finished=finished,
            unfinished_count=unfinished_count,
        )

        rolling_upgrade_res.additional_properties = d
        return rolling_upgrade_res

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
