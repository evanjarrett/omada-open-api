from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_traffic_activity import DeviceTrafficActivity


T = TypeVar("T", bound="TrafficActivities")


@_attrs_define
class TrafficActivities:
    """
    Attributes:
        ap_traffic_activities (Union[Unset, List['DeviceTrafficActivity']]): Wireless network total traffic timing list
        switch_traffic_activities (Union[Unset, List['DeviceTrafficActivity']]): Wireless network total traffic timing
            list Wired network total traffic timing list,
    """

    ap_traffic_activities: Union[Unset, List["DeviceTrafficActivity"]] = UNSET
    switch_traffic_activities: Union[Unset, List["DeviceTrafficActivity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ap_traffic_activities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ap_traffic_activities, Unset):
            ap_traffic_activities = []
            for ap_traffic_activities_item_data in self.ap_traffic_activities:
                ap_traffic_activities_item = ap_traffic_activities_item_data.to_dict()

                ap_traffic_activities.append(ap_traffic_activities_item)

        switch_traffic_activities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.switch_traffic_activities, Unset):
            switch_traffic_activities = []
            for switch_traffic_activities_item_data in self.switch_traffic_activities:
                switch_traffic_activities_item = switch_traffic_activities_item_data.to_dict()

                switch_traffic_activities.append(switch_traffic_activities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_traffic_activities is not UNSET:
            field_dict["apTrafficActivities"] = ap_traffic_activities
        if switch_traffic_activities is not UNSET:
            field_dict["switchTrafficActivities"] = switch_traffic_activities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_traffic_activity import DeviceTrafficActivity

        d = src_dict.copy()
        ap_traffic_activities = []
        _ap_traffic_activities = d.pop("apTrafficActivities", UNSET)
        for ap_traffic_activities_item_data in _ap_traffic_activities or []:
            ap_traffic_activities_item = DeviceTrafficActivity.from_dict(ap_traffic_activities_item_data)

            ap_traffic_activities.append(ap_traffic_activities_item)

        switch_traffic_activities = []
        _switch_traffic_activities = d.pop("switchTrafficActivities", UNSET)
        for switch_traffic_activities_item_data in _switch_traffic_activities or []:
            switch_traffic_activities_item = DeviceTrafficActivity.from_dict(switch_traffic_activities_item_data)

            switch_traffic_activities.append(switch_traffic_activities_item)

        traffic_activities = cls(
            ap_traffic_activities=ap_traffic_activities,
            switch_traffic_activities=switch_traffic_activities,
        )

        traffic_activities.additional_properties = d
        return traffic_activities

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
