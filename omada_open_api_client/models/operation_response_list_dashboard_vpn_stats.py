from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_vpn_stats import DashboardVpnStats


T = TypeVar("T", bound="OperationResponseListDashboardVpnStats")


@_attrs_define
class OperationResponseListDashboardVpnStats:
    """
    Attributes:
        error_code (Union[Unset, int]):
        msg (Union[Unset, str]):
        result (Union[Unset, List['DashboardVpnStats']]):
    """

    error_code: Union[Unset, int] = UNSET
    msg: Union[Unset, str] = UNSET
    result: Union[Unset, List["DashboardVpnStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code
        msg = self.msg
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()

                result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_vpn_stats import DashboardVpnStats

        d = src_dict.copy()
        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = DashboardVpnStats.from_dict(result_item_data)

            result.append(result_item)

        operation_response_list_dashboard_vpn_stats = cls(
            error_code=error_code,
            msg=msg,
            result=result,
        )

        operation_response_list_dashboard_vpn_stats.additional_properties = d
        return operation_response_list_dashboard_vpn_stats

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
