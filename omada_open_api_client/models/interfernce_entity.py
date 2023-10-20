from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interference_data_entity import InterferenceDataEntity


T = TypeVar("T", bound="InterfernceEntity")


@_attrs_define
class InterfernceEntity:
    """At most two types of interference data are reported in Inter, sorted in descending order of interference intensity

    Attributes:
        inf (Union[Unset, int]): interfernce, range [-96, -48]
        inf_type (Union[Unset, int]): Interference Type, range [0， 4]. 0 means invalid parameter, 1 means MWO, 2 means
            CW, and 4 means FHSS.
        inf_data (Union[Unset, InterferenceDataEntity]): Interference data, the data refer to the interference intensity
            and the times of interferences, and they are used to create histograms.
    """

    inf: Union[Unset, int] = UNSET
    inf_type: Union[Unset, int] = UNSET
    inf_data: Union[Unset, "InterferenceDataEntity"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inf = self.inf
        inf_type = self.inf_type
        inf_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inf_data, Unset):
            inf_data = self.inf_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inf is not UNSET:
            field_dict["inf"] = inf
        if inf_type is not UNSET:
            field_dict["infType"] = inf_type
        if inf_data is not UNSET:
            field_dict["infData"] = inf_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interference_data_entity import InterferenceDataEntity

        d = src_dict.copy()
        inf = d.pop("inf", UNSET)

        inf_type = d.pop("infType", UNSET)

        _inf_data = d.pop("infData", UNSET)
        inf_data: Union[Unset, InterferenceDataEntity]
        if isinstance(_inf_data, Unset):
            inf_data = UNSET
        else:
            inf_data = InterferenceDataEntity.from_dict(_inf_data)

        interfernce_entity = cls(
            inf=inf,
            inf_type=inf_type,
            inf_data=inf_data,
        )

        interfernce_entity.additional_properties = d
        return interfernce_entity

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
