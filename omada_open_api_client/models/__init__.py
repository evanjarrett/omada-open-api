""" Contains all the data models used in inputs/outputs """

from .access_token_detail_vo import AccessTokenDetailVO
from .access_token_response_v0 import AccessTokenResponseV0
from .access_token_v0 import AccessTokenV0
from .active_device import ActiveDevice
from .adopt_device_request_info import AdoptDeviceRequestInfo
from .adopt_device_result_info import AdoptDeviceResultInfo
from .ap_brief_info_vo import ApBriefInfoVO
from .ap_channel_stat_vo import ApChannelStatVO
from .ap_channels_stat_vo import ApChannelsStatVO
from .ap_general_config_entity import APGeneralConfigEntity
from .ap_interference import ApInterference
from .ap_interferences import ApInterferences
from .ap_overview_entity import APOverviewEntity
from .ap_radio_channel_entity import APRadioChannelEntity
from .ap_radio_setting_entity import APRadioSettingEntity
from .ap_radio_traffic_entity import APRadioTrafficEntity
from .ap_radios_config_entity import APRadiosConfigEntity
from .ap_radios_entity import APRadiosEntity
from .ap_uplinkwired_entity import APUplinkwiredEntity
from .ap_wired_uplink_entity import APWiredUplinkEntity
from .ap_wireless_uplink_entity import APWirelessUplinkEntity
from .apip_settings_entity import APIPSettingsEntity
from .aplan_entity import APLANEntity
from .aplan_traffic_entity import APLANTrafficEntity
from .aprf_scan_entity import APRFScanEntity
from .auth_client_open_api_vo import AuthClientOpenApiVO
from .auth_time_entity import AuthTimeEntity
from .band_ctrl_entity import BandCtrlEntity
from .batch_edit_tabs import BatchEditTabs
from .batch_update_given_switch_ports_profile_override_enable_setting_entity import (
    BatchUpdateGivenSwitchPortsProfileOverrideEnableSettingEntity,
)
from .batch_update_switch_ports_name_entity import BatchUpdateSwitchPortsNameEntity
from .batch_update_switch_ports_poe_entity import BatchUpdateSwitchPortsPoeEntity
from .batch_update_tab import BatchUpdateTab
from .channel_limit_setting_vo import ChannelLimitSettingVO
from .check_firmware_res import CheckFirmwareRes
from .client_grid_vo_client_info import ClientGridVOClientInfo
from .client_info import ClientInfo
from .client_ip_setting import ClientIpSetting
from .client_lock_to_ap_setting import ClientLockToApSetting
from .client_name_setting import ClientNameSetting
from .client_rate_limit_setting import ClientRateLimitSetting
from .client_stat_vo import ClientStatVO
from .client_to_site_vpn_client_entity import ClientToSiteVPNClientEntity
from .client_to_site_vpn_server_entity import ClientToSiteVPNServerEntity
from .controller_role_detail_vo import ControllerRoleDetailVO
from .controller_role_vo import ControllerRoleVO
from .cpu_usage import CpuUsage
from .create_role_result_vo import CreateRoleResultVO
from .create_site_entity import CreateSiteEntity
from .create_tab import CreateTab
from .create_user_result_vo import CreateUserResultVO
from .create_user_vo import CreateUserVO
from .created_res_id_open_api_vo import CreatedResIdOpenApiVO
from .custom_rate_limit_entity import CustomRateLimitEntity
from .dashboard_vpn_stats import DashboardVpnStats
from .delete_user_vo import DeleteUserVO
from .device_firmware_info import DeviceFirmwareInfo
from .device_info import DeviceInfo
from .device_location_detail_vo import DeviceLocationDetailVO
from .device_traffic_activity import DeviceTrafficActivity
from .device_traffic_distribution import DeviceTrafficDistribution
from .dhcp_ip_setting_entity import DhcpIpSettingEntity
from .dhcp_l2_relay_entity import DhcpL2RelayEntity
from .drop import Drop
from .drop_eap import DropEap
from .extend_time_entity import ExtendTimeEntity
from .form_auth_card_answer_open_api_vo import FormAuthCardAnswerOpenApiVO
from .form_auth_card_entity import FormAuthCardEntity
from .form_auth_entity import FormAuthEntity
from .form_auth_open_api_vo import FormAuthOpenApiVO
from .form_auth_result_open_api_vo import FormAuthResultOpenApiVO
from .gateway_info_entity import GatewayInfoEntity
from .gateway_lan_status_entity import GatewayLanStatusEntity
from .gateway_port_config_entity import GatewayPortConfigEntity
from .gateway_port_setting_config_entity import GatewayPortSettingConfigEntity
from .gateway_ports_config_entity import GatewayPortsConfigEntity
from .gateway_wan_status_entity import GatewayWanStatusEntity
from .get_access_token_grant_type import GetAccessTokenGrantType
from .get_dashboard_overview import GetDashboardOverview
from .grid_vo_auth_client_open_api_vo import GridVOAuthClientOpenApiVO
from .grid_vo_device_info import GridVODeviceInfo
from .grid_vo_form_auth_result_open_api_vo import GridVOFormAuthResultOpenApiVO
from .grid_vo_lan_profile_entity import GridVOLanProfileEntity
from .grid_vo_local_user_open_api_vo import GridVOLocalUserOpenApiVO
from .grid_vo_site_summary_info import GridVOSiteSummaryInfo
from .grid_vo_user_detail_vo import GridVOUserDetailVO
from .grid_vo_wire_guard_entity import GridVOWireGuardEntity
from .grid_vo_wire_guard_peer_entity import GridVOWireGuardPeerEntity
from .grid_vosslvpn_lock_entity import GridVOSSLVPNLockEntity
from .grid_vosslvpn_resource_entity import GridVOSSLVPNResourceEntity
from .grid_vosslvpn_resource_group_entity import GridVOSSLVPNResourceGroupEntity
from .grid_vosslvpn_user_group_entity import GridVOSSLVPNUserGroupEntity
from .interference_data_entity import InterferenceDataEntity
from .interfernce_entity import InterfernceEntity
from .ip_subnets_vo import IPSubnetsVO
from .ipsec_vpn_stats import IpsecVpnStats
from .isp_load import IspLoad
from .isp_load_stat import IspLoadStat
from .lan_profile_entity import LanProfileEntity
from .lan_profile_entity_tag_bridge_vlan_map import LanProfileEntityTagBridgeVlanMap
from .lan_profile_entity_untag_bridge_vlan_map import LanProfileEntityUntagBridgeVlanMap
from .list_tabs import ListTabs
from .local_user_entity import LocalUserEntity
from .local_user_open_api_vo import LocalUserOpenApiVO
from .locate_device_request_info import LocateDeviceRequestInfo
from .mem_usage import MemUsage
from .mesh_setting_vo import MeshSettingVO
from .modify_controller_role_vo import ModifyControllerRoleVO
from .modify_user_vo import ModifyUserVO
from .multi_link_item_vo import MultiLinkItemVO
from .online_upgrade_res import OnlineUpgradeRes
from .operation_response_adopt_device_result_info import OperationResponseAdoptDeviceResultInfo
from .operation_response_ap_channels_stat_vo import OperationResponseApChannelsStatVO
from .operation_response_ap_general_config_entity import OperationResponseAPGeneralConfigEntity
from .operation_response_ap_interferences import OperationResponseApInterferences
from .operation_response_ap_overview_entity import OperationResponseAPOverviewEntity
from .operation_response_ap_radios_config_entity import OperationResponseAPRadiosConfigEntity
from .operation_response_ap_radios_entity import OperationResponseAPRadiosEntity
from .operation_response_ap_uplinkwired_entity import OperationResponseAPUplinkwiredEntity
from .operation_response_apip_settings_entity import OperationResponseAPIPSettingsEntity
from .operation_response_aplan_entity import OperationResponseAPLANEntity
from .operation_response_aprf_scan_entity import OperationResponseAPRFScanEntity
from .operation_response_check_firmware_res import OperationResponseCheckFirmwareRes
from .operation_response_client_grid_vo_client_info import OperationResponseClientGridVOClientInfo
from .operation_response_client_info import OperationResponseClientInfo
from .operation_response_client_to_site_vpn_client_entity import OperationResponseClientToSiteVPNClientEntity
from .operation_response_client_to_site_vpn_server_entity import OperationResponseClientToSiteVPNServerEntity
from .operation_response_controller_role_detail_vo import OperationResponseControllerRoleDetailVO
from .operation_response_create_role_result_vo import OperationResponseCreateRoleResultVO
from .operation_response_create_user_result_vo import OperationResponseCreateUserResultVO
from .operation_response_created_res_id_open_api_vo import OperationResponseCreatedResIdOpenApiVO
from .operation_response_device_firmware_info import OperationResponseDeviceFirmwareInfo
from .operation_response_form_auth_open_api_vo import OperationResponseFormAuthOpenApiVO
from .operation_response_form_auth_result_open_api_vo import OperationResponseFormAuthResultOpenApiVO
from .operation_response_gateway_info_entity import OperationResponseGatewayInfoEntity
from .operation_response_gateway_port_setting_config_entity import OperationResponseGatewayPortSettingConfigEntity
from .operation_response_gateway_ports_config_entity import OperationResponseGatewayPortsConfigEntity
from .operation_response_get_dashboard_overview import OperationResponseGetDashboardOverview
from .operation_response_grid_vo_auth_client_open_api_vo import OperationResponseGridVOAuthClientOpenApiVO
from .operation_response_grid_vo_device_info import OperationResponseGridVODeviceInfo
from .operation_response_grid_vo_form_auth_result_open_api_vo import OperationResponseGridVOFormAuthResultOpenApiVO
from .operation_response_grid_vo_lan_profile_entity import OperationResponseGridVOLanProfileEntity
from .operation_response_grid_vo_local_user_open_api_vo import OperationResponseGridVOLocalUserOpenApiVO
from .operation_response_grid_vo_site_summary_info import OperationResponseGridVOSiteSummaryInfo
from .operation_response_grid_vo_user_detail_vo import OperationResponseGridVOUserDetailVO
from .operation_response_grid_vo_wire_guard_entity import OperationResponseGridVOWireGuardEntity
from .operation_response_grid_vo_wire_guard_peer_entity import OperationResponseGridVOWireGuardPeerEntity
from .operation_response_grid_vosslvpn_lock_entity import OperationResponseGridVOSSLVPNLockEntity
from .operation_response_grid_vosslvpn_resource_entity import OperationResponseGridVOSSLVPNResourceEntity
from .operation_response_grid_vosslvpn_resource_group_entity import OperationResponseGridVOSSLVPNResourceGroupEntity
from .operation_response_grid_vosslvpn_user_group_entity import OperationResponseGridVOSSLVPNUserGroupEntity
from .operation_response_list_active_device import OperationResponseListActiveDevice
from .operation_response_list_client_to_site_vpn_client_entity import OperationResponseListClientToSiteVPNClientEntity
from .operation_response_list_client_to_site_vpn_server_entity import OperationResponseListClientToSiteVPNServerEntity
from .operation_response_list_controller_role_detail_vo import OperationResponseListControllerRoleDetailVO
from .operation_response_list_cpu_usage import OperationResponseListCpuUsage
from .operation_response_list_dashboard_vpn_stats import OperationResponseListDashboardVpnStats
from .operation_response_list_form_auth_open_api_vo import OperationResponseListFormAuthOpenApiVO
from .operation_response_list_gateway_lan_status_entity import OperationResponseListGatewayLanStatusEntity
from .operation_response_list_gateway_wan_status_entity import OperationResponseListGatewayWanStatusEntity
from .operation_response_list_ipsec_vpn_stats import OperationResponseListIpsecVpnStats
from .operation_response_list_isp_load import OperationResponseListIspLoad
from .operation_response_list_list_tabs import OperationResponseListListTabs
from .operation_response_list_mem_usage import OperationResponseListMemUsage
from .operation_response_list_poe_usage import OperationResponseListPoeUsage
from .operation_response_list_portal_res_open_api_vo import OperationResponseListPortalResOpenApiVO
from .operation_response_list_rate_limit_profile_info import OperationResponseListRateLimitProfileInfo
from .operation_response_list_site_to_site_vpn_entity import OperationResponseListSiteToSiteVPNEntity
from .operation_response_list_string import OperationResponseListString
from .operation_response_list_vpn_user_entity import OperationResponseListVPNUserEntity
from .operation_response_local_user_open_api_vo import OperationResponseLocalUserOpenApiVO
from .operation_response_object import OperationResponseObject
from .operation_response_object_result import OperationResponseObjectResult
from .operation_response_online_upgrade_res import OperationResponseOnlineUpgradeRes
from .operation_response_retry_drop_rate import OperationResponseRetryDropRate
from .operation_response_rolling_upgrade_res import OperationResponseRollingUpgradeRes
from .operation_response_site_entity import OperationResponseSiteEntity
from .operation_response_site_setting_device_account import OperationResponseSiteSettingDeviceAccount
from .operation_response_site_settingchannel_limit import OperationResponseSiteSettingchannelLimit
from .operation_response_site_settingled import OperationResponseSiteSettingled
from .operation_response_site_settinglldp import OperationResponseSiteSettinglldp
from .operation_response_site_settingmesh import OperationResponseSiteSettingmesh
from .operation_response_site_settingremote_logging import OperationResponseSiteSettingremoteLogging
from .operation_response_site_to_site_vpn_entity import OperationResponseSiteToSiteVPNEntity
from .operation_response_ssl_vpn_user_open_api_grid_vosslvpn_user_entity import (
    OperationResponseSslVpnUserOpenApiGridVOSSLVPNUserEntity,
)
from .operation_response_sslvpn_server_entity import OperationResponseSSLVPNServerEntity
from .operation_response_switch_overview_entity import OperationResponseSwitchOverviewEntity
from .operation_response_switch_summary import OperationResponseSwitchSummary
from .operation_response_task_id import OperationResponseTaskId
from .operation_response_traffic_activities import OperationResponseTrafficActivities
from .operation_response_traffic_distribution import OperationResponseTrafficDistribution
from .operation_response_user_detail_vo import OperationResponseUserDetailVO
from .operation_response_wifi_summary import OperationResponseWifiSummary
from .operation_response_without_result import OperationResponseWithoutResult
from .osg_lan_port_ipv_6_config_vo import OsgLanPortIpv6ConfigVO
from .osg_wan_port_ipv_4_config_vo import OsgWanPortIpv4ConfigVO
from .osg_wan_port_ipv_6_config_vo import OsgWanPortIpv6ConfigVO
from .poe_usage import PoeUsage
from .port_info_entity import PortInfoEntity
from .port_poe import PortPoe
from .portal_res_open_api_vo import PortalResOpenApiVO
from .rate_limit_entity import RateLimitEntity
from .rate_limit_profile_info import RateLimitProfileInfo
from .remote_log_setting_vo import RemoteLogSettingVO
from .retry import Retry
from .retry_drop_rate import RetryDropRate
from .retry_eap import RetryEap
from .rf_scan_radio_entity import RFScanRadioEntity
from .rolling_upgrade_request_info import RollingUpgradeRequestInfo
from .rolling_upgrade_res import RollingUpgradeRes
from .scenario import Scenario
from .site_ap_lldp_setting_vo import SiteApLldpSettingVO
from .site_entity import SiteEntity
from .site_setting_device_account import SiteSettingDeviceAccount
from .site_settingchannel_limit import SiteSettingchannelLimit
from .site_settingled import SiteSettingled
from .site_settinglldp import SiteSettinglldp
from .site_settingmesh import SiteSettingmesh
from .site_settingremote_logging import SiteSettingremoteLogging
from .site_summary_info import SiteSummaryInfo
from .site_to_site_vpn_entity import SiteToSiteVPNEntity
from .spanning_tree_entity import SpanningTreeEntity
from .ssl_vpn_user_open_api_grid_vosslvpn_user_entity import SslVpnUserOpenApiGridVOSSLVPNUserEntity
from .sslvpn_lock_entity import SSLVPNLockEntity
from .sslvpn_resource_brief_entity import SSLVPNResourceBriefEntity
from .sslvpn_resource_brief_group_entity import SSLVPNResourceBriefGroupEntity
from .sslvpn_resource_entity import SSLVPNResourceEntity
from .sslvpn_resource_group_entity import SSLVPNResourceGroupEntity
from .sslvpn_server_entity import SSLVPNServerEntity
from .sslvpn_user_entity import SSLVPNUserEntity
from .sslvpn_user_group_entity import SSLVPNUserGroupEntity
from .static_ip_setting_entity import StaticIpSettingEntity
from .storm_ctrl_entity import StormCtrlEntity
from .switch_overview_entity import SwitchOverviewEntity
from .switch_port_and_name import SwitchPortAndName
from .switch_summary import SwitchSummary
from .task_id import TaskId
from .traffic_activities import TrafficActivities
from .traffic_distribution import TrafficDistribution
from .update_site_entity import UpdateSiteEntity
from .update_tab import UpdateTab
from .update_the_given_switch_port_name_entity import UpdateTheGivenSwitchPortNameEntity
from .update_the_given_switch_port_profile_entity import UpdateTheGivenSwitchPortProfileEntity
from .update_the_given_switch_port_profile_override_enable_setting_entity import (
    UpdateTheGivenSwitchPortProfileOverrideEnableSettingEntity,
)
from .update_the_switch_port_poe_entity import UpdateTheSwitchPortPoeEntity
from .user_detail_vo import UserDetailVO
from .vpn_user_entity import VPNUserEntity
from .wifi_summary import WifiSummary
from .wire_guard_entity import WireGuardEntity
from .wire_guard_peer_entity import WireGuardPeerEntity

__all__ = (
    "AccessTokenDetailVO",
    "AccessTokenResponseV0",
    "AccessTokenV0",
    "ActiveDevice",
    "AdoptDeviceRequestInfo",
    "AdoptDeviceResultInfo",
    "ApBriefInfoVO",
    "ApChannelsStatVO",
    "ApChannelStatVO",
    "APGeneralConfigEntity",
    "ApInterference",
    "ApInterferences",
    "APIPSettingsEntity",
    "APLANEntity",
    "APLANTrafficEntity",
    "APOverviewEntity",
    "APRadioChannelEntity",
    "APRadiosConfigEntity",
    "APRadiosEntity",
    "APRadioSettingEntity",
    "APRadioTrafficEntity",
    "APRFScanEntity",
    "APUplinkwiredEntity",
    "APWiredUplinkEntity",
    "APWirelessUplinkEntity",
    "AuthClientOpenApiVO",
    "AuthTimeEntity",
    "BandCtrlEntity",
    "BatchEditTabs",
    "BatchUpdateGivenSwitchPortsProfileOverrideEnableSettingEntity",
    "BatchUpdateSwitchPortsNameEntity",
    "BatchUpdateSwitchPortsPoeEntity",
    "BatchUpdateTab",
    "ChannelLimitSettingVO",
    "CheckFirmwareRes",
    "ClientGridVOClientInfo",
    "ClientInfo",
    "ClientIpSetting",
    "ClientLockToAPSetting",
    "ClientLockToApSetting",
    "ClientNameSetting",
    "ClientRateLimitSetting",
    "ClientStatVO",
    "ClientToSiteVPNClientEntity",
    "ClientToSiteVPNServerEntity",
    "ControllerRoleDetailVO",
    "ControllerRoleVO",
    "CpuUsage",
    "CreatedResIdOpenApiVO",
    "CreateRoleResultVO",
    "CreateSiteEntity",
    "CreateTab",
    "CreateUserResultVO",
    "CreateUserVO",
    "CustomRateLimitEntity",
    "DashboardVpnStats",
    "DeleteUserVO",
    "DeviceFirmwareInfo",
    "DeviceInfo",
    "DeviceLocationDetailVO",
    "DeviceTrafficActivity",
    "DeviceTrafficDistribution",
    "DhcpIpSettingEntity",
    "DhcpL2RelayEntity",
    "Drop",
    "DropEap",
    "ExtendTimeEntity",
    "FormAuthCardAnswerOpenApiVO",
    "FormAuthCardEntity",
    "FormAuthEntity",
    "FormAuthOpenApiVO",
    "FormAuthResultOpenApiVO",
    "GatewayInfoEntity",
    "GatewayLanStatusEntity",
    "GatewayPortConfigEntity",
    "GatewayPortsConfigEntity",
    "GatewayPortSettingConfigEntity",
    "GatewayWanStatusEntity",
    "GetAccessTokenGrantType",
    "GetDashboardOverview",
    "GridVOAuthClientOpenApiVO",
    "GridVODeviceInfo",
    "GridVOFormAuthResultOpenApiVO",
    "GridVOLanProfileEntity",
    "GridVOLocalUserOpenApiVO",
    "GridVOSiteSummaryInfo",
    "GridVOSSLVPNLockEntity",
    "GridVOSSLVPNResourceEntity",
    "GridVOSSLVPNResourceGroupEntity",
    "GridVOSSLVPNUserGroupEntity",
    "GridVOUserDetailVO",
    "GridVOWireGuardEntity",
    "GridVOWireGuardPeerEntity",
    "InterferenceDataEntity",
    "InterfernceEntity",
    "IpsecVpnStats",
    "IPSubnetsVO",
    "IspLoad",
    "IspLoadStat",
    "LanProfileEntity",
    "LanProfileEntityTagBridgeVlanMap",
    "LanProfileEntityUntagBridgeVlanMap",
    "ListTabs",
    "LocalUserEntity",
    "LocalUserOpenApiVO",
    "LocateDeviceRequestInfo",
    "MemUsage",
    "MeshSettingVO",
    "ModifyControllerRoleVO",
    "ModifyUserVO",
    "MultiLinkItemVO",
    "OnlineUpgradeRes",
    "OperationResponseAdoptDeviceResultInfo",
    "OperationResponseApChannelsStatVO",
    "OperationResponseAPGeneralConfigEntity",
    "OperationResponseApInterferences",
    "OperationResponseAPIPSettingsEntity",
    "OperationResponseAPLANEntity",
    "OperationResponseAPOverviewEntity",
    "OperationResponseAPRadiosConfigEntity",
    "OperationResponseAPRadiosEntity",
    "OperationResponseAPRFScanEntity",
    "OperationResponseAPUplinkwiredEntity",
    "OperationResponseCheckFirmwareRes",
    "OperationResponseClientGridVOClientInfo",
    "OperationResponseClientInfo",
    "OperationResponseClientToSiteVPNClientEntity",
    "OperationResponseClientToSiteVPNServerEntity",
    "OperationResponseControllerRoleDetailVO",
    "OperationResponseCreatedResIdOpenApiVO",
    "OperationResponseCreateRoleResultVO",
    "OperationResponseCreateUserResultVO",
    "OperationResponseDeviceFirmwareInfo",
    "OperationResponseFormAuthOpenApiVO",
    "OperationResponseFormAuthResultOpenApiVO",
    "OperationResponseGatewayInfoEntity",
    "OperationResponseGatewayPortsConfigEntity",
    "OperationResponseGatewayPortSettingConfigEntity",
    "OperationResponseGetDashboardOverview",
    "OperationResponseGridVOAuthClientOpenApiVO",
    "OperationResponseGridVODeviceInfo",
    "OperationResponseGridVOFormAuthResultOpenApiVO",
    "OperationResponseGridVOLanProfileEntity",
    "OperationResponseGridVOLocalUserOpenApiVO",
    "OperationResponseGridVOSiteSummaryInfo",
    "OperationResponseGridVOSSLVPNLockEntity",
    "OperationResponseGridVOSSLVPNResourceEntity",
    "OperationResponseGridVOSSLVPNResourceGroupEntity",
    "OperationResponseGridVOSSLVPNUserGroupEntity",
    "OperationResponseGridVOUserDetailVO",
    "OperationResponseGridVOWireGuardEntity",
    "OperationResponseGridVOWireGuardPeerEntity",
    "OperationResponseListActiveDevice",
    "OperationResponseListClientToSiteVPNClientEntity",
    "OperationResponseListClientToSiteVPNServerEntity",
    "OperationResponseListControllerRoleDetailVO",
    "OperationResponseListCpuUsage",
    "OperationResponseListDashboardVpnStats",
    "OperationResponseListFormAuthOpenApiVO",
    "OperationResponseListGatewayLanStatusEntity",
    "OperationResponseListGatewayWanStatusEntity",
    "OperationResponseListIpsecVpnStats",
    "OperationResponseListIspLoad",
    "OperationResponseListListTabs",
    "OperationResponseListMemUsage",
    "OperationResponseListPoeUsage",
    "OperationResponseListPortalResOpenApiVO",
    "OperationResponseListRateLimitProfileInfo",
    "OperationResponseListSiteToSiteVPNEntity",
    "OperationResponseListString",
    "OperationResponseListVPNUserEntity",
    "OperationResponseLocalUserOpenApiVO",
    "OperationResponseObject",
    "OperationResponseObjectResult",
    "OperationResponseOnlineUpgradeRes",
    "OperationResponseRetryDropRate",
    "OperationResponseRollingUpgradeRes",
    "OperationResponseSiteEntity",
    "OperationResponseSiteSettingchannelLimit",
    "OperationResponseSiteSettingDeviceAccount",
    "OperationResponseSiteSettingled",
    "OperationResponseSiteSettinglldp",
    "OperationResponseSiteSettingmesh",
    "OperationResponseSiteSettingremoteLogging",
    "OperationResponseSiteToSiteVPNEntity",
    "OperationResponseSSLVPNServerEntity",
    "OperationResponseSslVpnUserOpenApiGridVOSSLVPNUserEntity",
    "OperationResponseSwitchOverviewEntity",
    "OperationResponseSwitchSummary",
    "OperationResponseTaskId",
    "OperationResponseTrafficActivities",
    "OperationResponseTrafficDistribution",
    "OperationResponseUserDetailVO",
    "OperationResponseWifiSummary",
    "OperationResponseWithoutResult",
    "OsgLanPortIpv6ConfigVO",
    "OsgWanPortIpv4ConfigVO",
    "OsgWanPortIpv6ConfigVO",
    "PoeUsage",
    "PortalResOpenApiVO",
    "PortInfoEntity",
    "PortPoe",
    "RateLimitEntity",
    "RateLimitProfileInfo",
    "RemoteLogSettingVO",
    "Retry",
    "RetryDropRate",
    "RetryEap",
    "RFScanRadioEntity",
    "RollingUpgradeRequestInfo",
    "RollingUpgradeRes",
    "Scenario",
    "SiteApLldpSettingVO",
    "SiteEntity",
    "SiteSettingchannelLimit",
    "SiteSettingDeviceAccount",
    "SiteSettingled",
    "SiteSettinglldp",
    "SiteSettingmesh",
    "SiteSettingremoteLogging",
    "SiteSummaryInfo",
    "SiteToSiteVPNEntity",
    "SpanningTreeEntity",
    "SSLVPNLockEntity",
    "SSLVPNResourceBriefEntity",
    "SSLVPNResourceBriefGroupEntity",
    "SSLVPNResourceEntity",
    "SSLVPNResourceGroupEntity",
    "SSLVPNServerEntity",
    "SSLVPNUserEntity",
    "SSLVPNUserGroupEntity",
    "SslVpnUserOpenApiGridVOSSLVPNUserEntity",
    "StaticIpSettingEntity",
    "StormCtrlEntity",
    "SwitchOverviewEntity",
    "SwitchPortAndName",
    "SwitchSummary",
    "TaskId",
    "TrafficActivities",
    "TrafficDistribution",
    "UpdateSiteEntity",
    "UpdateTab",
    "UpdateTheGivenSwitchPortNameEntity",
    "UpdateTheGivenSwitchPortProfileEntity",
    "UpdateTheGivenSwitchPortProfileOverrideEnableSettingEntity",
    "UpdateTheSwitchPortPoeEntity",
    "UserDetailVO",
    "VPNUserEntity",
    "WifiSummary",
    "WireGuardEntity",
    "WireGuardPeerEntity",
)
