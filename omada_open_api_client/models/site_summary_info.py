from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSummaryInfo")


@_attrs_define
class SiteSummaryInfo:
    """
    Attributes:
        site_id (Union[Unset, str]): Site ID
        name (Union[Unset, str]): site name
        region (Union[Unset, str]): site region
        time_zone (Union[Unset, str]): site timeZone
        scenario (Union[Unset, str]): site scenario
        longitude (Union[Unset, float]): site longitude
        latitude (Union[Unset, float]): site latitude
        address (Union[Unset, str]): site address
        type (Union[Unset, int]): site type(only for pro controller). 0:Basic Site; 1:Pro Site
    """

    site_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    scenario: Union[Unset, str] = UNSET
    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    address: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site_id = self.site_id
        name = self.name
        region = self.region
        time_zone = self.time_zone
        scenario = self.scenario
        longitude = self.longitude
        latitude = self.latitude
        address = self.address
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        scenario = d.pop("scenario", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        type = d.pop("type", UNSET)

        site_summary_info = cls(
            site_id=site_id,
            name=name,
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            longitude=longitude,
            latitude=latitude,
            address=address,
            type=type,
        )

        site_summary_info.additional_properties = d
        return site_summary_info

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
