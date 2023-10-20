from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceLocationDetailVO")


@_attrs_define
class DeviceLocationDetailVO:
    """device location

    Attributes:
        longitude (Union[Unset, float]):
        latitude (Union[Unset, float]):
        address (Union[Unset, str]):
    """

    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        longitude = self.longitude
        latitude = self.latitude
        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        device_location_detail_vo = cls(
            longitude=longitude,
            latitude=latitude,
            address=address,
        )

        device_location_detail_vo.additional_properties = d
        return device_location_detail_vo

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
