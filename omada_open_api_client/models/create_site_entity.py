from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_setting_device_account import SiteSettingDeviceAccount


T = TypeVar("T", bound="CreateSiteEntity")


@_attrs_define
class CreateSiteEntity:
    """
    Attributes:
        name (str): Name of the site
        region (str): Country of the site
        time_zone (str): Timezone of the site
        scenario (str): Scenario of the site
        device_account_setting (SiteSettingDeviceAccount):
        type (Union[Unset, int]): site type(only for pro controller). 0:Basic Site; 1:Pro Site
        longitude (Union[Unset, float]): Longitude of the site should between -180 and 180.
        latitude (Union[Unset, float]): Latitude of the site should between -90 and 90.
        address (Union[Unset, str]): Address of the site
    """

    name: str
    region: str
    time_zone: str
    scenario: str
    device_account_setting: "SiteSettingDeviceAccount"
    type: Union[Unset, int] = UNSET
    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        region = self.region
        time_zone = self.time_zone
        scenario = self.scenario
        device_account_setting = self.device_account_setting.to_dict()

        type = self.type
        longitude = self.longitude
        latitude = self.latitude
        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "region": region,
                "timeZone": time_zone,
                "scenario": scenario,
                "deviceAccountSetting": device_account_setting,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_setting_device_account import SiteSettingDeviceAccount

        d = src_dict.copy()
        name = d.pop("name")

        region = d.pop("region")

        time_zone = d.pop("timeZone")

        scenario = d.pop("scenario")

        device_account_setting = SiteSettingDeviceAccount.from_dict(d.pop("deviceAccountSetting"))

        type = d.pop("type", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        create_site_entity = cls(
            name=name,
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            device_account_setting=device_account_setting,
            type=type,
            longitude=longitude,
            latitude=latitude,
            address=address,
        )

        create_site_entity.additional_properties = d
        return create_site_entity

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
