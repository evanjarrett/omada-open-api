from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APRadioTrafficEntity")


@_attrs_define
class APRadioTrafficEntity:
    """radio traffic 6g

    Attributes:
        rx_pkts (Union[Unset, int]): total rx packets
        tx_pkts (Union[Unset, int]): total tx packets
        rx (Union[Unset, int]): total rx bytes
        tx (Union[Unset, int]): total tx bytes
        rx_drop_pkts (Union[Unset, int]): rx dropped packets
        tx_drop_pkts (Union[Unset, int]): tx dropped Packets
        rx_err_pkts (Union[Unset, int]): rx error packets
        tx_err_pkts (Union[Unset, int]): tx error packets
        rx_retry_pkts (Union[Unset, int]): rx retried packets
        tx_retry_pkts (Union[Unset, int]): tx retried packets
    """

    rx_pkts: Union[Unset, int] = UNSET
    tx_pkts: Union[Unset, int] = UNSET
    rx: Union[Unset, int] = UNSET
    tx: Union[Unset, int] = UNSET
    rx_drop_pkts: Union[Unset, int] = UNSET
    tx_drop_pkts: Union[Unset, int] = UNSET
    rx_err_pkts: Union[Unset, int] = UNSET
    tx_err_pkts: Union[Unset, int] = UNSET
    rx_retry_pkts: Union[Unset, int] = UNSET
    tx_retry_pkts: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rx_pkts = self.rx_pkts
        tx_pkts = self.tx_pkts
        rx = self.rx
        tx = self.tx
        rx_drop_pkts = self.rx_drop_pkts
        tx_drop_pkts = self.tx_drop_pkts
        rx_err_pkts = self.rx_err_pkts
        tx_err_pkts = self.tx_err_pkts
        rx_retry_pkts = self.rx_retry_pkts
        tx_retry_pkts = self.tx_retry_pkts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rx_pkts is not UNSET:
            field_dict["rxPkts"] = rx_pkts
        if tx_pkts is not UNSET:
            field_dict["txPkts"] = tx_pkts
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if rx_retry_pkts is not UNSET:
            field_dict["rxRetryPkts"] = rx_retry_pkts
        if tx_retry_pkts is not UNSET:
            field_dict["txRetryPkts"] = tx_retry_pkts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rx_pkts = d.pop("rxPkts", UNSET)

        tx_pkts = d.pop("txPkts", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        rx_retry_pkts = d.pop("rxRetryPkts", UNSET)

        tx_retry_pkts = d.pop("txRetryPkts", UNSET)

        ap_radio_traffic_entity = cls(
            rx_pkts=rx_pkts,
            tx_pkts=tx_pkts,
            rx=rx,
            tx=tx,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
            rx_retry_pkts=rx_retry_pkts,
            tx_retry_pkts=tx_retry_pkts,
        )

        ap_radio_traffic_entity.additional_properties = d
        return ap_radio_traffic_entity

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
