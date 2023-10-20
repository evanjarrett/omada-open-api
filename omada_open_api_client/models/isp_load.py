from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_load_stat import IspLoadStat


T = TypeVar("T", bound="IspLoad")


@_attrs_define
class IspLoad:
    """
    Attributes:
        port_id (Union[Unset, int]): port ID
        port_name (Union[Unset, str]): port name
        data (Union[Unset, List['IspLoadStat']]): WAN port data list
    """

    port_id: Union[Unset, int] = UNSET
    port_name: Union[Unset, str] = UNSET
    data: Union[Unset, List["IspLoadStat"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port_id = self.port_id
        port_name = self.port_name
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.isp_load_stat import IspLoadStat

        d = src_dict.copy()
        port_id = d.pop("portId", UNSET)

        port_name = d.pop("portName", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = IspLoadStat.from_dict(data_item_data)

            data.append(data_item)

        isp_load = cls(
            port_id=port_id,
            port_name=port_name,
            data=data,
        )

        isp_load.additional_properties = d
        return isp_load

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
