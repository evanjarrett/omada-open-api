from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_entity import RateLimitEntity


T = TypeVar("T", bound="LocalUserEntity")


@_attrs_define
class LocalUserEntity:
    """
    Attributes:
        user_name (str): User name. 1~128 ASCII visible characters, with no spaces at the beginning and end, and spaces
            in the middle
        password (str): Password. Length of PassWord is from 1 to 128.
        enable (bool): Whether to enable.
        expiration_time (int): Expiration time.
        binding_type (int): MAC binding type, 0:no binding; 1:static binding; 2:dynamic binding.
        max_users (int): The maximum number of users online at the same time when the MAC binding type is No Binding. It
            cannot be modified after initialization. Value of Maximum Users is from 1 to 2048.
        rate_limit (RateLimitEntity): When configuring rate limit, can only configure one of rateLimitProfileId or
            customRateLimit.
        traffic_limit_enable (bool): Whether to enable traffic limit.
        portals (List[str]): Bound portal IDs.
        mac_address (Union[Unset, str]): Mac address,the value is only available when the macType is static binding or
            dynamic binding.
        name (Union[Unset, str]): Name. Allow any characters from 1 to 128, with no spaces at the beginning and end, and
            spaces in the middle
        phone (Union[Unset, str]): Phone number.Length of Telephone is from 1 to 20.
        traffic_limit (Union[Unset, int]): Traffic limit in MB.Value of limit is from 1 to 10485760 MB.
        traffic_limit_frequency (Union[Unset, int]): Frequency of traffic limit. daily: 1, weekly: 2, monthly: 3, total:
            0;.
    """

    user_name: str
    password: str
    enable: bool
    expiration_time: int
    binding_type: int
    max_users: int
    rate_limit: "RateLimitEntity"
    traffic_limit_enable: bool
    portals: List[str]
    mac_address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    traffic_limit: Union[Unset, int] = UNSET
    traffic_limit_frequency: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        password = self.password
        enable = self.enable
        expiration_time = self.expiration_time
        binding_type = self.binding_type
        max_users = self.max_users
        rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable
        portals = self.portals

        mac_address = self.mac_address
        name = self.name
        phone = self.phone
        traffic_limit = self.traffic_limit
        traffic_limit_frequency = self.traffic_limit_frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "password": password,
                "enable": enable,
                "expirationTime": expiration_time,
                "bindingType": binding_type,
                "maxUsers": max_users,
                "rateLimit": rate_limit,
                "trafficLimitEnable": traffic_limit_enable,
                "portals": portals,
            }
        )
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rate_limit_entity import RateLimitEntity

        d = src_dict.copy()
        user_name = d.pop("userName")

        password = d.pop("password")

        enable = d.pop("enable")

        expiration_time = d.pop("expirationTime")

        binding_type = d.pop("bindingType")

        max_users = d.pop("maxUsers")

        rate_limit = RateLimitEntity.from_dict(d.pop("rateLimit"))

        traffic_limit_enable = d.pop("trafficLimitEnable")

        portals = cast(List[str], d.pop("portals"))

        mac_address = d.pop("macAddress", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        local_user_entity = cls(
            user_name=user_name,
            password=password,
            enable=enable,
            expiration_time=expiration_time,
            binding_type=binding_type,
            max_users=max_users,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            portals=portals,
            mac_address=mac_address,
            name=name,
            phone=phone,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
        )

        local_user_entity.additional_properties = d
        return local_user_entity

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
