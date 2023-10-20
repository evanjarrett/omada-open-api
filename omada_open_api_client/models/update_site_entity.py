from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSiteEntity")


@_attrs_define
class UpdateSiteEntity:
    """
    Attributes:
        region (str): site region
        time_zone (str): site timeZone
        scenario (str): site scenario
        name (Union[Unset, str]): site name
        longitude (Union[Unset, float]): site longitude
        latitude (Union[Unset, float]): site latitude
        address (Union[Unset, str]): site address
    """

    region: str
    time_zone: str
    scenario: str
    name: Union[Unset, str] = UNSET
    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region = self.region
        time_zone = self.time_zone
        scenario = self.scenario
        name = self.name
        longitude = self.longitude
        latitude = self.latitude
        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "timeZone": time_zone,
                "scenario": scenario,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
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
        region = d.pop("region")

        time_zone = d.pop("timeZone")

        scenario = d.pop("scenario")

        name = d.pop("name", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        update_site_entity = cls(
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            name=name,
            longitude=longitude,
            latitude=latitude,
            address=address,
        )

        update_site_entity.additional_properties = d
        return update_site_entity

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
