from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpanningTreeEntity")


@_attrs_define
class SpanningTreeEntity:
    """spanningTreeSetting

    Attributes:
        priority (int): range from 0 to 240
        prioext_path_costrity (int): range from 0 to 2000000
        int_path_cost (int): range from 0 to 2000000
        edge_port (bool): edgePort status
        p_2_p_link (int): range from 0 to 2
        mcheck (Union[Unset, bool]): mcheck
        loop_protect (Union[Unset, bool]): loopProtect
        root_protect (Union[Unset, bool]): rootProtect
        tc_guard (Union[Unset, bool]): tcGuard
        bpdu_protect (Union[Unset, bool]): bpduProtect
        bpdu_filter (Union[Unset, bool]): bpduFilter
        bpdu_forward (Union[Unset, bool]): bpduForward
    """

    priority: int
    prioext_path_costrity: int
    int_path_cost: int
    edge_port: bool
    p_2_p_link: int
    mcheck: Union[Unset, bool] = UNSET
    loop_protect: Union[Unset, bool] = UNSET
    root_protect: Union[Unset, bool] = UNSET
    tc_guard: Union[Unset, bool] = UNSET
    bpdu_protect: Union[Unset, bool] = UNSET
    bpdu_filter: Union[Unset, bool] = UNSET
    bpdu_forward: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        priority = self.priority
        prioext_path_costrity = self.prioext_path_costrity
        int_path_cost = self.int_path_cost
        edge_port = self.edge_port
        p_2_p_link = self.p_2_p_link
        mcheck = self.mcheck
        loop_protect = self.loop_protect
        root_protect = self.root_protect
        tc_guard = self.tc_guard
        bpdu_protect = self.bpdu_protect
        bpdu_filter = self.bpdu_filter
        bpdu_forward = self.bpdu_forward

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
                "prioextPathCostrity": prioext_path_costrity,
                "intPathCost": int_path_cost,
                "edgePort": edge_port,
                "p2pLink": p_2_p_link,
            }
        )
        if mcheck is not UNSET:
            field_dict["mcheck"] = mcheck
        if loop_protect is not UNSET:
            field_dict["loopProtect"] = loop_protect
        if root_protect is not UNSET:
            field_dict["rootProtect"] = root_protect
        if tc_guard is not UNSET:
            field_dict["tcGuard"] = tc_guard
        if bpdu_protect is not UNSET:
            field_dict["bpduProtect"] = bpdu_protect
        if bpdu_filter is not UNSET:
            field_dict["bpduFilter"] = bpdu_filter
        if bpdu_forward is not UNSET:
            field_dict["bpduForward"] = bpdu_forward

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        priority = d.pop("priority")

        prioext_path_costrity = d.pop("prioextPathCostrity")

        int_path_cost = d.pop("intPathCost")

        edge_port = d.pop("edgePort")

        p_2_p_link = d.pop("p2pLink")

        mcheck = d.pop("mcheck", UNSET)

        loop_protect = d.pop("loopProtect", UNSET)

        root_protect = d.pop("rootProtect", UNSET)

        tc_guard = d.pop("tcGuard", UNSET)

        bpdu_protect = d.pop("bpduProtect", UNSET)

        bpdu_filter = d.pop("bpduFilter", UNSET)

        bpdu_forward = d.pop("bpduForward", UNSET)

        spanning_tree_entity = cls(
            priority=priority,
            prioext_path_costrity=prioext_path_costrity,
            int_path_cost=int_path_cost,
            edge_port=edge_port,
            p_2_p_link=p_2_p_link,
            mcheck=mcheck,
            loop_protect=loop_protect,
            root_protect=root_protect,
            tc_guard=tc_guard,
            bpdu_protect=bpdu_protect,
            bpdu_filter=bpdu_filter,
            bpdu_forward=bpdu_forward,
        )

        spanning_tree_entity.additional_properties = d
        return spanning_tree_entity

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
