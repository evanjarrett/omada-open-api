from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rf_scan_radio_entity import RFScanRadioEntity


T = TypeVar("T", bound="APRFScanEntity")


@_attrs_define
class APRFScanEntity:
    """
    Attributes:
        channel2g (Union[Unset, List['RFScanRadioEntity']]): channel 2g
        channel5g (Union[Unset, List['RFScanRadioEntity']]): channel 5g
        channel5g2 (Union[Unset, List['RFScanRadioEntity']]): channel 5g2
        channel6g (Union[Unset, List['RFScanRadioEntity']]): channel 6g
        current_chan_2_g (Union[Unset, str]): The 2G channel of AP, such as 1,6,11,13, range: 1~13
        current_chan_5_g (Union[Unset, str]): The 5G channel of AP, such as 36,161, range: 36~161
        current_chan_5_g_2 (Union[Unset, str]): The 5G2 channel of AP,such as 36,161, range: 36~161
        current_chan_6_g (Union[Unset, str]): The 6G channel of AP,such as 36,161, range: 36~161
        current_chan_w2_g (Union[Unset, int]): The 2g channel bandwidth of the AP, the value range: {2, 3}, 2 means
            20MHz, 3 means 40MHz
        current_chan_w5_g (Union[Unset, int]): The 5g channel bandwidth of the AP, the value range: {2, 3, 5}, 2 menas
            20MHz, 3 means 40MHz, 5 means 80MHz
        current_chan_w5_g_2 (Union[Unset, int]): The 5g2 channel bandwidth of the AP, the value range: {2, 3, 5}, 2
            menas 20MHz, 3 means 40MHz, 5 means 80MHz
        current_chan_w6_g (Union[Unset, int]): The 6g channel bandwidth of the AP, the value range: {2, 3, 5}, 2 menas
            20MHz, 3 means 40MHz, 5 means 80MHz
        time (Union[Unset, int]): The scan time(13 bits)
        status (Union[Unset, int]): 0: the scan result is displayed;1: no scan result;2: Scanning;
    """

    channel2g: Union[Unset, List["RFScanRadioEntity"]] = UNSET
    channel5g: Union[Unset, List["RFScanRadioEntity"]] = UNSET
    channel5g2: Union[Unset, List["RFScanRadioEntity"]] = UNSET
    channel6g: Union[Unset, List["RFScanRadioEntity"]] = UNSET
    current_chan_2_g: Union[Unset, str] = UNSET
    current_chan_5_g: Union[Unset, str] = UNSET
    current_chan_5_g_2: Union[Unset, str] = UNSET
    current_chan_6_g: Union[Unset, str] = UNSET
    current_chan_w2_g: Union[Unset, int] = UNSET
    current_chan_w5_g: Union[Unset, int] = UNSET
    current_chan_w5_g_2: Union[Unset, int] = UNSET
    current_chan_w6_g: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel2g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel2g, Unset):
            channel2g = []
            for channel2g_item_data in self.channel2g:
                channel2g_item = channel2g_item_data.to_dict()

                channel2g.append(channel2g_item)

        channel5g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel5g, Unset):
            channel5g = []
            for channel5g_item_data in self.channel5g:
                channel5g_item = channel5g_item_data.to_dict()

                channel5g.append(channel5g_item)

        channel5g2: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel5g2, Unset):
            channel5g2 = []
            for channel5g2_item_data in self.channel5g2:
                channel5g2_item = channel5g2_item_data.to_dict()

                channel5g2.append(channel5g2_item)

        channel6g: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel6g, Unset):
            channel6g = []
            for channel6g_item_data in self.channel6g:
                channel6g_item = channel6g_item_data.to_dict()

                channel6g.append(channel6g_item)

        current_chan_2_g = self.current_chan_2_g
        current_chan_5_g = self.current_chan_5_g
        current_chan_5_g_2 = self.current_chan_5_g_2
        current_chan_6_g = self.current_chan_6_g
        current_chan_w2_g = self.current_chan_w2_g
        current_chan_w5_g = self.current_chan_w5_g
        current_chan_w5_g_2 = self.current_chan_w5_g_2
        current_chan_w6_g = self.current_chan_w6_g
        time = self.time
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel2g is not UNSET:
            field_dict["channel2g"] = channel2g
        if channel5g is not UNSET:
            field_dict["channel5g"] = channel5g
        if channel5g2 is not UNSET:
            field_dict["channel5g2"] = channel5g2
        if channel6g is not UNSET:
            field_dict["channel6g"] = channel6g
        if current_chan_2_g is not UNSET:
            field_dict["currentChan2g"] = current_chan_2_g
        if current_chan_5_g is not UNSET:
            field_dict["currentChan5g"] = current_chan_5_g
        if current_chan_5_g_2 is not UNSET:
            field_dict["currentChan5g2"] = current_chan_5_g_2
        if current_chan_6_g is not UNSET:
            field_dict["currentChan6g"] = current_chan_6_g
        if current_chan_w2_g is not UNSET:
            field_dict["currentChanW2g"] = current_chan_w2_g
        if current_chan_w5_g is not UNSET:
            field_dict["currentChanW5g"] = current_chan_w5_g
        if current_chan_w5_g_2 is not UNSET:
            field_dict["currentChanW5g2"] = current_chan_w5_g_2
        if current_chan_w6_g is not UNSET:
            field_dict["currentChanW6g"] = current_chan_w6_g
        if time is not UNSET:
            field_dict["time"] = time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rf_scan_radio_entity import RFScanRadioEntity

        d = src_dict.copy()
        channel2g = []
        _channel2g = d.pop("channel2g", UNSET)
        for channel2g_item_data in _channel2g or []:
            channel2g_item = RFScanRadioEntity.from_dict(channel2g_item_data)

            channel2g.append(channel2g_item)

        channel5g = []
        _channel5g = d.pop("channel5g", UNSET)
        for channel5g_item_data in _channel5g or []:
            channel5g_item = RFScanRadioEntity.from_dict(channel5g_item_data)

            channel5g.append(channel5g_item)

        channel5g2 = []
        _channel5g2 = d.pop("channel5g2", UNSET)
        for channel5g2_item_data in _channel5g2 or []:
            channel5g2_item = RFScanRadioEntity.from_dict(channel5g2_item_data)

            channel5g2.append(channel5g2_item)

        channel6g = []
        _channel6g = d.pop("channel6g", UNSET)
        for channel6g_item_data in _channel6g or []:
            channel6g_item = RFScanRadioEntity.from_dict(channel6g_item_data)

            channel6g.append(channel6g_item)

        current_chan_2_g = d.pop("currentChan2g", UNSET)

        current_chan_5_g = d.pop("currentChan5g", UNSET)

        current_chan_5_g_2 = d.pop("currentChan5g2", UNSET)

        current_chan_6_g = d.pop("currentChan6g", UNSET)

        current_chan_w2_g = d.pop("currentChanW2g", UNSET)

        current_chan_w5_g = d.pop("currentChanW5g", UNSET)

        current_chan_w5_g_2 = d.pop("currentChanW5g2", UNSET)

        current_chan_w6_g = d.pop("currentChanW6g", UNSET)

        time = d.pop("time", UNSET)

        status = d.pop("status", UNSET)

        aprf_scan_entity = cls(
            channel2g=channel2g,
            channel5g=channel5g,
            channel5g2=channel5g2,
            channel6g=channel6g,
            current_chan_2_g=current_chan_2_g,
            current_chan_5_g=current_chan_5_g,
            current_chan_5_g_2=current_chan_5_g_2,
            current_chan_6_g=current_chan_6_g,
            current_chan_w2_g=current_chan_w2_g,
            current_chan_w5_g=current_chan_w5_g,
            current_chan_w5_g_2=current_chan_w5_g_2,
            current_chan_w6_g=current_chan_w6_g,
            time=time,
            status=status,
        )

        aprf_scan_entity.additional_properties = d
        return aprf_scan_entity

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
