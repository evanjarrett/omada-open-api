from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerRoleVO")


@_attrs_define
class ControllerRoleVO:
    """role privilege

    Attributes:
        license_ (Union[Unset, int]): License permission. 0:block; 1:view only; 2:modify
        global_dashboard (Union[Unset, int]): Dashboard permission in global view. 0:block; 1:view only; 2:modify
        dashboard (Union[Unset, int]): Dashboard permission in site view. 0:block; 1:view only; 2:modify
        devices (Union[Unset, int]): Devices permission in site view and global view. 0:block; 1:view only; 2:modify
        adopt (Union[Unset, int]): Adopt permission 0:block; 2:access
        add_devices (Union[Unset, int]): Add devices permission 0:block; 2:access
        manual_upgrade (Union[Unset, int]): Manual Upgrade permission 0:block; 2:access
        global_log (Union[Unset, int]): Log permission in global view. 0:block; 1:view only; 2:modify
        log (Union[Unset, int]): Log permission in site view. 0:block; 1:view only; 2:modify
        license_bind (Union[Unset, int]): License bind permission. 0:block; 1:view only; 2:modify
        users (Union[Unset, int]): Users permission in global view. 0:block; 1:view only; 2:modify
        roles (Union[Unset, int]): Roles permission in global view. 0:block; 1:view only; 2:modify
        saml_users (Union[Unset, int]): Saml users permission in global view. 0:block; 1:view only; 2:modify
        saml_roles (Union[Unset, int]): Saml roles permission in global view. 0:block; 1:view only; 2:modify
        saml_ssos (Union[Unset, int]): Saml ssos permission in global view. 0:block; 1:view only; 2:modify
        global_setting (Union[Unset, int]): Settings permission in global view. 0:block; 1:view only; 2:modify
        export_data (Union[Unset, int]): Export data permission in site view. 0:block; 2:access
        global_export_data (Union[Unset, int]): Export data permission in global view. 0:block; 2:access
        export_global_log (Union[Unset, int]): Export global log data permission in global view. 0:block; 2:access
        hotspot (Union[Unset, int]): Hotspot permission. 0:block; 1:view only; 2:modify
        statics (Union[Unset, int]): Statics permission in site view. 0:block; 1:view only; 2:modify
        map_ (Union[Unset, int]): Map permission in site view. 0:block; 1:view only; 2:modify
        clients (Union[Unset, int]): Clients permission in site view. 0:block; 1:view only; 2:modify
        insight (Union[Unset, int]): Insight permission in site view. 0:block; 1:view only; 2:modify
        report (Union[Unset, int]): Network report permission in site view. 0:block; 1:view only; 2:modify
        network (Union[Unset, int]): Site network settings permission in site view -> settings. 0:block; 1:view only;
            2:modify
        device_account (Union[Unset, int]): Device account permission in site view -> site settings. 0:block; 1:view
            only; 2:modify
        anomaly (Union[Unset, int]): Anomaly permission in global view. 0:block; 1:view only; 2:modify
        analyze (Union[Unset, int]): Tools permission in global view. Only for hardware controller. 0:block; 1:view
            only; 2:modify
        site_analyze (Union[Unset, int]): Tools in site view. 0:block; 1:view only; 2:modify
        global_security (Union[Unset, int]): Security permission in global view. 0:block; 1:view only; 2:modify
        global_webhook (Union[Unset, int]): webhook in global view, only for pro controller
        global_map_token (Union[Unset, int]): MapToken in global view, only for pro controller
    """

    license_: Union[Unset, int] = UNSET
    global_dashboard: Union[Unset, int] = UNSET
    dashboard: Union[Unset, int] = UNSET
    devices: Union[Unset, int] = UNSET
    adopt: Union[Unset, int] = UNSET
    add_devices: Union[Unset, int] = UNSET
    manual_upgrade: Union[Unset, int] = UNSET
    global_log: Union[Unset, int] = UNSET
    log: Union[Unset, int] = UNSET
    license_bind: Union[Unset, int] = UNSET
    users: Union[Unset, int] = UNSET
    roles: Union[Unset, int] = UNSET
    saml_users: Union[Unset, int] = UNSET
    saml_roles: Union[Unset, int] = UNSET
    saml_ssos: Union[Unset, int] = UNSET
    global_setting: Union[Unset, int] = UNSET
    export_data: Union[Unset, int] = UNSET
    global_export_data: Union[Unset, int] = UNSET
    export_global_log: Union[Unset, int] = UNSET
    hotspot: Union[Unset, int] = UNSET
    statics: Union[Unset, int] = UNSET
    map_: Union[Unset, int] = UNSET
    clients: Union[Unset, int] = UNSET
    insight: Union[Unset, int] = UNSET
    report: Union[Unset, int] = UNSET
    network: Union[Unset, int] = UNSET
    device_account: Union[Unset, int] = UNSET
    anomaly: Union[Unset, int] = UNSET
    analyze: Union[Unset, int] = UNSET
    site_analyze: Union[Unset, int] = UNSET
    global_security: Union[Unset, int] = UNSET
    global_webhook: Union[Unset, int] = UNSET
    global_map_token: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_ = self.license_
        global_dashboard = self.global_dashboard
        dashboard = self.dashboard
        devices = self.devices
        adopt = self.adopt
        add_devices = self.add_devices
        manual_upgrade = self.manual_upgrade
        global_log = self.global_log
        log = self.log
        license_bind = self.license_bind
        users = self.users
        roles = self.roles
        saml_users = self.saml_users
        saml_roles = self.saml_roles
        saml_ssos = self.saml_ssos
        global_setting = self.global_setting
        export_data = self.export_data
        global_export_data = self.global_export_data
        export_global_log = self.export_global_log
        hotspot = self.hotspot
        statics = self.statics
        map_ = self.map_
        clients = self.clients
        insight = self.insight
        report = self.report
        network = self.network
        device_account = self.device_account
        anomaly = self.anomaly
        analyze = self.analyze
        site_analyze = self.site_analyze
        global_security = self.global_security
        global_webhook = self.global_webhook
        global_map_token = self.global_map_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_ is not UNSET:
            field_dict["license"] = license_
        if global_dashboard is not UNSET:
            field_dict["globalDashboard"] = global_dashboard
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if devices is not UNSET:
            field_dict["devices"] = devices
        if adopt is not UNSET:
            field_dict["adopt"] = adopt
        if add_devices is not UNSET:
            field_dict["addDevices"] = add_devices
        if manual_upgrade is not UNSET:
            field_dict["manualUpgrade"] = manual_upgrade
        if global_log is not UNSET:
            field_dict["globalLog"] = global_log
        if log is not UNSET:
            field_dict["log"] = log
        if license_bind is not UNSET:
            field_dict["licenseBind"] = license_bind
        if users is not UNSET:
            field_dict["users"] = users
        if roles is not UNSET:
            field_dict["roles"] = roles
        if saml_users is not UNSET:
            field_dict["samlUsers"] = saml_users
        if saml_roles is not UNSET:
            field_dict["samlRoles"] = saml_roles
        if saml_ssos is not UNSET:
            field_dict["samlSsos"] = saml_ssos
        if global_setting is not UNSET:
            field_dict["globalSetting"] = global_setting
        if export_data is not UNSET:
            field_dict["exportData"] = export_data
        if global_export_data is not UNSET:
            field_dict["globalExportData"] = global_export_data
        if export_global_log is not UNSET:
            field_dict["exportGlobalLog"] = export_global_log
        if hotspot is not UNSET:
            field_dict["hotspot"] = hotspot
        if statics is not UNSET:
            field_dict["statics"] = statics
        if map_ is not UNSET:
            field_dict["map"] = map_
        if clients is not UNSET:
            field_dict["clients"] = clients
        if insight is not UNSET:
            field_dict["insight"] = insight
        if report is not UNSET:
            field_dict["report"] = report
        if network is not UNSET:
            field_dict["network"] = network
        if device_account is not UNSET:
            field_dict["deviceAccount"] = device_account
        if anomaly is not UNSET:
            field_dict["anomaly"] = anomaly
        if analyze is not UNSET:
            field_dict["analyze"] = analyze
        if site_analyze is not UNSET:
            field_dict["siteAnalyze"] = site_analyze
        if global_security is not UNSET:
            field_dict["globalSecurity"] = global_security
        if global_webhook is not UNSET:
            field_dict["globalWebhook"] = global_webhook
        if global_map_token is not UNSET:
            field_dict["globalMapToken"] = global_map_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        license_ = d.pop("license", UNSET)

        global_dashboard = d.pop("globalDashboard", UNSET)

        dashboard = d.pop("dashboard", UNSET)

        devices = d.pop("devices", UNSET)

        adopt = d.pop("adopt", UNSET)

        add_devices = d.pop("addDevices", UNSET)

        manual_upgrade = d.pop("manualUpgrade", UNSET)

        global_log = d.pop("globalLog", UNSET)

        log = d.pop("log", UNSET)

        license_bind = d.pop("licenseBind", UNSET)

        users = d.pop("users", UNSET)

        roles = d.pop("roles", UNSET)

        saml_users = d.pop("samlUsers", UNSET)

        saml_roles = d.pop("samlRoles", UNSET)

        saml_ssos = d.pop("samlSsos", UNSET)

        global_setting = d.pop("globalSetting", UNSET)

        export_data = d.pop("exportData", UNSET)

        global_export_data = d.pop("globalExportData", UNSET)

        export_global_log = d.pop("exportGlobalLog", UNSET)

        hotspot = d.pop("hotspot", UNSET)

        statics = d.pop("statics", UNSET)

        map_ = d.pop("map", UNSET)

        clients = d.pop("clients", UNSET)

        insight = d.pop("insight", UNSET)

        report = d.pop("report", UNSET)

        network = d.pop("network", UNSET)

        device_account = d.pop("deviceAccount", UNSET)

        anomaly = d.pop("anomaly", UNSET)

        analyze = d.pop("analyze", UNSET)

        site_analyze = d.pop("siteAnalyze", UNSET)

        global_security = d.pop("globalSecurity", UNSET)

        global_webhook = d.pop("globalWebhook", UNSET)

        global_map_token = d.pop("globalMapToken", UNSET)

        controller_role_vo = cls(
            license_=license_,
            global_dashboard=global_dashboard,
            dashboard=dashboard,
            devices=devices,
            adopt=adopt,
            add_devices=add_devices,
            manual_upgrade=manual_upgrade,
            global_log=global_log,
            log=log,
            license_bind=license_bind,
            users=users,
            roles=roles,
            saml_users=saml_users,
            saml_roles=saml_roles,
            saml_ssos=saml_ssos,
            global_setting=global_setting,
            export_data=export_data,
            global_export_data=global_export_data,
            export_global_log=export_global_log,
            hotspot=hotspot,
            statics=statics,
            map_=map_,
            clients=clients,
            insight=insight,
            report=report,
            network=network,
            device_account=device_account,
            anomaly=anomaly,
            analyze=analyze,
            site_analyze=site_analyze,
            global_security=global_security,
            global_webhook=global_webhook,
            global_map_token=global_map_token,
        )

        controller_role_vo.additional_properties = d
        return controller_role_vo

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
