from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.switch_port_and_name import SwitchPortAndName


T = TypeVar("T", bound="BatchUpdateSwitchPortsNameEntity")


@_attrs_define
class BatchUpdateSwitchPortsNameEntity:
    """
    Attributes:
        port_name_list (List['SwitchPortAndName']): portNameList
    """

    port_name_list: List["SwitchPortAndName"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port_name_list = []
        for port_name_list_item_data in self.port_name_list:
            port_name_list_item = port_name_list_item_data.to_dict()

            port_name_list.append(port_name_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portNameList": port_name_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.switch_port_and_name import SwitchPortAndName

        d = src_dict.copy()
        port_name_list = []
        _port_name_list = d.pop("portNameList")
        for port_name_list_item_data in _port_name_list:
            port_name_list_item = SwitchPortAndName.from_dict(port_name_list_item_data)

            port_name_list.append(port_name_list_item)

        batch_update_switch_ports_name_entity = cls(
            port_name_list=port_name_list,
        )

        batch_update_switch_ports_name_entity.additional_properties = d
        return batch_update_switch_ports_name_entity

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
