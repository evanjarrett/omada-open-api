from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_entity import RateLimitEntity


T = TypeVar("T", bound="LocalUserOpenApiVO")


@_attrs_define
class LocalUserOpenApiVO:
    """
    Attributes:
        id (Union[Unset, str]): Local user id
        user_name (Union[Unset, str]): User name
        password (Union[Unset, str]): Password
        enable (Union[Unset, bool]): Whether to enable.
        expiration_time (Union[Unset, int]): Expiration time
        binding_type (Union[Unset, int]): MAC binding type, 0:no binding; 1:static binding; 2:dynamic binding.
        mac_address (Union[Unset, str]): Mac address,the value is only available when the macType is static binding or
            dynamic binding.
        max_users (Union[Unset, int]): The maximum number of users online at the same time when the MAC binding type is
            No Binding. It cannot be modified after initialization. Value of Maximum Users is from 1 to 2048.
        name (Union[Unset, str]): Name
        phone (Union[Unset, str]): Phone number.
        rate_limit (Union[Unset, RateLimitEntity]): When configuring rate limit, can only configure one of
            rateLimitProfileId or customRateLimit.
        traffic_limit_enable (Union[Unset, bool]): Whether to enable traffic limit.
        traffic_limit (Union[Unset, int]): Traffic limit in MB.Value of limit is from 1 to 10485760 MB.
        traffic_left (Union[Unset, bool]): Is there any remaining traffic.
        traffic_used (Union[Unset, int]): Used traffic(MB).
        traffic_limit_frequency (Union[Unset, int]): Frequency of traffic limit. daily: 1, weekly: 2, monthly: 3, total:
            0;.
        used (Union[Unset, int]): Used quantity.
        overtime (Union[Unset, bool]): Whether the current time has exceeded the expirationTime
        portals (Union[Unset, List[str]]): Bound portal names.
    """

    id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    expiration_time: Union[Unset, int] = UNSET
    binding_type: Union[Unset, int] = UNSET
    mac_address: Union[Unset, str] = UNSET
    max_users: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    rate_limit: Union[Unset, "RateLimitEntity"] = UNSET
    traffic_limit_enable: Union[Unset, bool] = UNSET
    traffic_limit: Union[Unset, int] = UNSET
    traffic_left: Union[Unset, bool] = UNSET
    traffic_used: Union[Unset, int] = UNSET
    traffic_limit_frequency: Union[Unset, int] = UNSET
    used: Union[Unset, int] = UNSET
    overtime: Union[Unset, bool] = UNSET
    portals: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_name = self.user_name
        password = self.password
        enable = self.enable
        expiration_time = self.expiration_time
        binding_type = self.binding_type
        mac_address = self.mac_address
        max_users = self.max_users
        name = self.name
        phone = self.phone
        rate_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable
        traffic_limit = self.traffic_limit
        traffic_left = self.traffic_left
        traffic_used = self.traffic_used
        traffic_limit_frequency = self.traffic_limit_frequency
        used = self.used
        overtime = self.overtime
        portals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.portals, Unset):
            portals = self.portals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if enable is not UNSET:
            field_dict["enable"] = enable
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if binding_type is not UNSET:
            field_dict["bindingType"] = binding_type
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if max_users is not UNSET:
            field_dict["maxUsers"] = max_users
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if traffic_limit_enable is not UNSET:
            field_dict["trafficLimitEnable"] = traffic_limit_enable
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_left is not UNSET:
            field_dict["trafficLeft"] = traffic_left
        if traffic_used is not UNSET:
            field_dict["trafficUsed"] = traffic_used
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if used is not UNSET:
            field_dict["used"] = used
        if overtime is not UNSET:
            field_dict["overtime"] = overtime
        if portals is not UNSET:
            field_dict["portals"] = portals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rate_limit_entity import RateLimitEntity

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_name = d.pop("userName", UNSET)

        password = d.pop("password", UNSET)

        enable = d.pop("enable", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        binding_type = d.pop("bindingType", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        max_users = d.pop("maxUsers", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: Union[Unset, RateLimitEntity]
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimitEntity.from_dict(_rate_limit)

        traffic_limit_enable = d.pop("trafficLimitEnable", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_left = d.pop("trafficLeft", UNSET)

        traffic_used = d.pop("trafficUsed", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        used = d.pop("used", UNSET)

        overtime = d.pop("overtime", UNSET)

        portals = cast(List[str], d.pop("portals", UNSET))

        local_user_open_api_vo = cls(
            id=id,
            user_name=user_name,
            password=password,
            enable=enable,
            expiration_time=expiration_time,
            binding_type=binding_type,
            mac_address=mac_address,
            max_users=max_users,
            name=name,
            phone=phone,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            traffic_limit=traffic_limit,
            traffic_left=traffic_left,
            traffic_used=traffic_used,
            traffic_limit_frequency=traffic_limit_frequency,
            used=used,
            overtime=overtime,
            portals=portals,
        )

        local_user_open_api_vo.additional_properties = d
        return local_user_open_api_vo

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
