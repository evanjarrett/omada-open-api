from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_traffic_distribution import DeviceTrafficDistribution


T = TypeVar("T", bound="TrafficDistribution")


@_attrs_define
class TrafficDistribution:
    """
    Attributes:
        aps (Union[Unset, List['DeviceTrafficDistribution']]): Current Site Ap List
        switches (Union[Unset, List['DeviceTrafficDistribution']]): Current Site Switch List
    """

    aps: Union[Unset, List["DeviceTrafficDistribution"]] = UNSET
    switches: Union[Unset, List["DeviceTrafficDistribution"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aps, Unset):
            aps = []
            for aps_item_data in self.aps:
                aps_item = aps_item_data.to_dict()

                aps.append(aps_item)

        switches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()

                switches.append(switches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aps is not UNSET:
            field_dict["aps"] = aps
        if switches is not UNSET:
            field_dict["switches"] = switches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_traffic_distribution import DeviceTrafficDistribution

        d = src_dict.copy()
        aps = []
        _aps = d.pop("aps", UNSET)
        for aps_item_data in _aps or []:
            aps_item = DeviceTrafficDistribution.from_dict(aps_item_data)

            aps.append(aps_item)

        switches = []
        _switches = d.pop("switches", UNSET)
        for switches_item_data in _switches or []:
            switches_item = DeviceTrafficDistribution.from_dict(switches_item_data)

            switches.append(switches_item)

        traffic_distribution = cls(
            aps=aps,
            switches=switches,
        )

        traffic_distribution.additional_properties = d
        return traffic_distribution

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
