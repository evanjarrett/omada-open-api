from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_ip_setting import ClientIpSetting
    from ..models.client_lock_to_ap_setting import ClientLockToApSetting
    from ..models.client_rate_limit_setting import ClientRateLimitSetting
    from ..models.multi_link_item_vo import MultiLinkItemVO


T = TypeVar("T", bound="ClientInfo")


@_attrs_define
class ClientInfo:
    """
    Attributes:
        id (Union[Unset, str]): Client ID
        mac (Union[Unset, str]): Client MAC Address
        name (Union[Unset, str]): Client Name, alias
        host_name (Union[Unset, str]): Host name, device name
        vendor (Union[Unset, str]): Vendor
        device_type (Union[Unset, str]): Device Type: iphone, ipod,android,pc,printer,tv...
        device_category (Union[Unset, str]): Device Category: loT, TV, computer, phone...
        os_name (Union[Unset, str]): Device system version
        ip (Union[Unset, str]): IP Address
        ipv_6_list (Union[Unset, List[str]]): IPv6 Address
        connect_type (Union[Unset, int]): Connect type  0: wireless guest  1: wireless user  2: wired user
        connect_dev_type (Union[Unset, str]): ap, switch, gateway
        connected_to_wireless_router (Union[Unset, bool]): true: Client is connecting to a wireless router.
        wireless (Union[Unset, bool]): true: Wireless device (connectDevType=ap)  false: Not wireless
            device(connectDevType=switch or gateway)
        ssid (Union[Unset, str]): (Wireless)  SSID name
        signal_level (Union[Unset, int]): (Wireless) Signal strength percentage, value range [0, 100]
        health_score (Union[Unset, int]): 1~3: poor, 4~7: fair, 0: no data, 8~10 good.
        signal_rank (Union[Unset, int]): (Wireless) Signal strength level, value range [0, 5]
        wifi_mode (Union[Unset, int]): (Wireless)  0: 11a  1: 11b  2: 11g  3: 11na  4: 11ng  5: 11ac  6: 11axa  7: 11axg
        ap_name (Union[Unset, str]): (Wireless)  AP Name
        ap_mac (Union[Unset, str]): (Wireless)  AP MAC Address
        radio_id (Union[Unset, int]): (Wireless)  0: 2.4GHz  1: 5GHz-1  2:5GHz-2 3: 6GHz
        channel (Union[Unset, int]): (Wireless)  Actual channel
        rx_rate (Union[Unset, int]): (Wireless) Uplink negotiation rate (Kbit/s)
        tx_rate (Union[Unset, int]): (Wireless) Downlink negotiation rate (Kbit/s)
        power_save (Union[Unset, bool]): (Wireless)  true: Power save mode enabled
        rssi (Union[Unset, int]): (Wireless) Signal strength, unit: dBm
        snr (Union[Unset, int]):
        switch_mac (Union[Unset, str]): (Wired, connectDevType=switch)  Switch MAC address
        switch_name (Union[Unset, str]): (Wired, connectDevType=switch)  Switch name
        gateway_mac (Union[Unset, str]): (Wired, connectDevType=gateway)  Gateway MAC Address
        gateway_name (Union[Unset, str]): (Wired, connectDevType=gateway)  Gateway name
        vid (Union[Unset, int]): (Wired), vlan
        network_name (Union[Unset, str]): (Wired) Network name
        dot_1_x_identity (Union[Unset, str]): (Wired) 802.1x authentication identity
        dot_1_x_vlan (Union[Unset, int]): (Wired) Network name corresponding to the VLAN obtained by 802.1x D-VLAN
        port (Union[Unset, int]): (Wired) Port ID
        lag_id (Union[Unset, int]): (Wired) LAG ID. Exists only when the client is connected to the LAG
        activity (Union[Unset, int]): Real-time downlink rate (Byte/s)
        traffic_down (Union[Unset, int]): Downstream traffic (Byte)
        traffic_up (Union[Unset, int]): Upstream traffic (Byte)
        uptime (Union[Unset, int]): Up time (unit: s)
        last_seen (Union[Unset, int]): Last found time, timestamp (ms)
        auth_status (Union[Unset, int]): Authentication status.0: CONNECTED // Access without any authentication
            method.1: PENDING // Access to Portal, but authentication failed.2: AUTHORIZED // Pass through portal, pass
            other authentication without portal.3: AUTH-FREE // No portal authentication required.
        blocked (Union[Unset, bool]): Whether the client is blocked
        guest (Union[Unset, bool]): (Wireless) Whether it is Guest (used to display the wireless Guest client icon)
        active (Union[Unset, bool]): Whether the client is online
        manager (Union[Unset, bool]): Whether it is the client currently being managed
        ip_setting (Union[Unset, ClientIpSetting]):
        down_packet (Union[Unset, int]): Number of downstream packets
        up_packet (Union[Unset, int]): Number of upstream packets
        rate_limit (Union[Unset, ClientRateLimitSetting]):
        client_lock_to_ap_setting (Union[Unset, ClientLockToApSetting]): Client lock to ap setting
        support5g2 (Union[Unset, bool]):
        multi_link (Union[Unset, List['MultiLinkItemVO']]):
        unit (Union[Unset, int]): unit id
        standard_port (Union[Unset, str]): standardPort
    """

    id: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    device_category: Union[Unset, str] = UNSET
    os_name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    ipv_6_list: Union[Unset, List[str]] = UNSET
    connect_type: Union[Unset, int] = UNSET
    connect_dev_type: Union[Unset, str] = UNSET
    connected_to_wireless_router: Union[Unset, bool] = UNSET
    wireless: Union[Unset, bool] = UNSET
    ssid: Union[Unset, str] = UNSET
    signal_level: Union[Unset, int] = UNSET
    health_score: Union[Unset, int] = UNSET
    signal_rank: Union[Unset, int] = UNSET
    wifi_mode: Union[Unset, int] = UNSET
    ap_name: Union[Unset, str] = UNSET
    ap_mac: Union[Unset, str] = UNSET
    radio_id: Union[Unset, int] = UNSET
    channel: Union[Unset, int] = UNSET
    rx_rate: Union[Unset, int] = UNSET
    tx_rate: Union[Unset, int] = UNSET
    power_save: Union[Unset, bool] = UNSET
    rssi: Union[Unset, int] = UNSET
    snr: Union[Unset, int] = UNSET
    switch_mac: Union[Unset, str] = UNSET
    switch_name: Union[Unset, str] = UNSET
    gateway_mac: Union[Unset, str] = UNSET
    gateway_name: Union[Unset, str] = UNSET
    vid: Union[Unset, int] = UNSET
    network_name: Union[Unset, str] = UNSET
    dot_1_x_identity: Union[Unset, str] = UNSET
    dot_1_x_vlan: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    lag_id: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    traffic_down: Union[Unset, int] = UNSET
    traffic_up: Union[Unset, int] = UNSET
    uptime: Union[Unset, int] = UNSET
    last_seen: Union[Unset, int] = UNSET
    auth_status: Union[Unset, int] = UNSET
    blocked: Union[Unset, bool] = UNSET
    guest: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    manager: Union[Unset, bool] = UNSET
    ip_setting: Union[Unset, "ClientIpSetting"] = UNSET
    down_packet: Union[Unset, int] = UNSET
    up_packet: Union[Unset, int] = UNSET
    rate_limit: Union[Unset, "ClientRateLimitSetting"] = UNSET
    client_lock_to_ap_setting: Union[Unset, "ClientLockToApSetting"] = UNSET
    support5g2: Union[Unset, bool] = UNSET
    multi_link: Union[Unset, List["MultiLinkItemVO"]] = UNSET
    unit: Union[Unset, int] = UNSET
    standard_port: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mac = self.mac
        name = self.name
        host_name = self.host_name
        vendor = self.vendor
        device_type = self.device_type
        device_category = self.device_category
        os_name = self.os_name
        ip = self.ip
        ipv_6_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        connect_type = self.connect_type
        connect_dev_type = self.connect_dev_type
        connected_to_wireless_router = self.connected_to_wireless_router
        wireless = self.wireless
        ssid = self.ssid
        signal_level = self.signal_level
        health_score = self.health_score
        signal_rank = self.signal_rank
        wifi_mode = self.wifi_mode
        ap_name = self.ap_name
        ap_mac = self.ap_mac
        radio_id = self.radio_id
        channel = self.channel
        rx_rate = self.rx_rate
        tx_rate = self.tx_rate
        power_save = self.power_save
        rssi = self.rssi
        snr = self.snr
        switch_mac = self.switch_mac
        switch_name = self.switch_name
        gateway_mac = self.gateway_mac
        gateway_name = self.gateway_name
        vid = self.vid
        network_name = self.network_name
        dot_1_x_identity = self.dot_1_x_identity
        dot_1_x_vlan = self.dot_1_x_vlan
        port = self.port
        lag_id = self.lag_id
        activity = self.activity
        traffic_down = self.traffic_down
        traffic_up = self.traffic_up
        uptime = self.uptime
        last_seen = self.last_seen
        auth_status = self.auth_status
        blocked = self.blocked
        guest = self.guest
        active = self.active
        manager = self.manager
        ip_setting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_setting, Unset):
            ip_setting = self.ip_setting.to_dict()

        down_packet = self.down_packet
        up_packet = self.up_packet
        rate_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        client_lock_to_ap_setting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_lock_to_ap_setting, Unset):
            client_lock_to_ap_setting = self.client_lock_to_ap_setting.to_dict()

        support5g2 = self.support5g2
        multi_link: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.multi_link, Unset):
            multi_link = []
            for multi_link_item_data in self.multi_link:
                multi_link_item = multi_link_item_data.to_dict()

                multi_link.append(multi_link_item)

        unit = self.unit
        standard_port = self.standard_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_category is not UNSET:
            field_dict["deviceCategory"] = device_category
        if os_name is not UNSET:
            field_dict["osName"] = os_name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if connect_type is not UNSET:
            field_dict["connectType"] = connect_type
        if connect_dev_type is not UNSET:
            field_dict["connectDevType"] = connect_dev_type
        if connected_to_wireless_router is not UNSET:
            field_dict["connectedToWirelessRouter"] = connected_to_wireless_router
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if signal_rank is not UNSET:
            field_dict["signalRank"] = signal_rank
        if wifi_mode is not UNSET:
            field_dict["wifiMode"] = wifi_mode
        if ap_name is not UNSET:
            field_dict["apName"] = ap_name
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if power_save is not UNSET:
            field_dict["powerSave"] = power_save
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if switch_mac is not UNSET:
            field_dict["switchMac"] = switch_mac
        if switch_name is not UNSET:
            field_dict["switchName"] = switch_name
        if gateway_mac is not UNSET:
            field_dict["gatewayMac"] = gateway_mac
        if gateway_name is not UNSET:
            field_dict["gatewayName"] = gateway_name
        if vid is not UNSET:
            field_dict["vid"] = vid
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if dot_1_x_identity is not UNSET:
            field_dict["dot1xIdentity"] = dot_1_x_identity
        if dot_1_x_vlan is not UNSET:
            field_dict["dot1xVlan"] = dot_1_x_vlan
        if port is not UNSET:
            field_dict["port"] = port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if activity is not UNSET:
            field_dict["activity"] = activity
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if guest is not UNSET:
            field_dict["guest"] = guest
        if active is not UNSET:
            field_dict["active"] = active
        if manager is not UNSET:
            field_dict["manager"] = manager
        if ip_setting is not UNSET:
            field_dict["ipSetting"] = ip_setting
        if down_packet is not UNSET:
            field_dict["downPacket"] = down_packet
        if up_packet is not UNSET:
            field_dict["upPacket"] = up_packet
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if client_lock_to_ap_setting is not UNSET:
            field_dict["clientLockToApSetting"] = client_lock_to_ap_setting
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if multi_link is not UNSET:
            field_dict["multiLink"] = multi_link
        if unit is not UNSET:
            field_dict["unit"] = unit
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_ip_setting import ClientIpSetting
        from ..models.client_lock_to_ap_setting import ClientLockToApSetting
        from ..models.client_rate_limit_setting import ClientRateLimitSetting
        from ..models.multi_link_item_vo import MultiLinkItemVO

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        host_name = d.pop("hostName", UNSET)

        vendor = d.pop("vendor", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_category = d.pop("deviceCategory", UNSET)

        os_name = d.pop("osName", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(List[str], d.pop("ipv6List", UNSET))

        connect_type = d.pop("connectType", UNSET)

        connect_dev_type = d.pop("connectDevType", UNSET)

        connected_to_wireless_router = d.pop("connectedToWirelessRouter", UNSET)

        wireless = d.pop("wireless", UNSET)

        ssid = d.pop("ssid", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        health_score = d.pop("healthScore", UNSET)

        signal_rank = d.pop("signalRank", UNSET)

        wifi_mode = d.pop("wifiMode", UNSET)

        ap_name = d.pop("apName", UNSET)

        ap_mac = d.pop("apMac", UNSET)

        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        power_save = d.pop("powerSave", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        switch_mac = d.pop("switchMac", UNSET)

        switch_name = d.pop("switchName", UNSET)

        gateway_mac = d.pop("gatewayMac", UNSET)

        gateway_name = d.pop("gatewayName", UNSET)

        vid = d.pop("vid", UNSET)

        network_name = d.pop("networkName", UNSET)

        dot_1_x_identity = d.pop("dot1xIdentity", UNSET)

        dot_1_x_vlan = d.pop("dot1xVlan", UNSET)

        port = d.pop("port", UNSET)

        lag_id = d.pop("lagId", UNSET)

        activity = d.pop("activity", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        uptime = d.pop("uptime", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        auth_status = d.pop("authStatus", UNSET)

        blocked = d.pop("blocked", UNSET)

        guest = d.pop("guest", UNSET)

        active = d.pop("active", UNSET)

        manager = d.pop("manager", UNSET)

        _ip_setting = d.pop("ipSetting", UNSET)
        ip_setting: Union[Unset, ClientIpSetting]
        if isinstance(_ip_setting, Unset):
            ip_setting = UNSET
        else:
            ip_setting = ClientIpSetting.from_dict(_ip_setting)

        down_packet = d.pop("downPacket", UNSET)

        up_packet = d.pop("upPacket", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: Union[Unset, ClientRateLimitSetting]
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = ClientRateLimitSetting.from_dict(_rate_limit)

        _client_lock_to_ap_setting = d.pop("clientLockToApSetting", UNSET)
        client_lock_to_ap_setting: Union[Unset, ClientLockToApSetting]
        if isinstance(_client_lock_to_ap_setting, Unset):
            client_lock_to_ap_setting = UNSET
        else:
            client_lock_to_ap_setting = ClientLockToApSetting.from_dict(_client_lock_to_ap_setting)

        support5g2 = d.pop("support5g2", UNSET)

        multi_link = []
        _multi_link = d.pop("multiLink", UNSET)
        for multi_link_item_data in _multi_link or []:
            multi_link_item = MultiLinkItemVO.from_dict(multi_link_item_data)

            multi_link.append(multi_link_item)

        unit = d.pop("unit", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        client_info = cls(
            id=id,
            mac=mac,
            name=name,
            host_name=host_name,
            vendor=vendor,
            device_type=device_type,
            device_category=device_category,
            os_name=os_name,
            ip=ip,
            ipv_6_list=ipv_6_list,
            connect_type=connect_type,
            connect_dev_type=connect_dev_type,
            connected_to_wireless_router=connected_to_wireless_router,
            wireless=wireless,
            ssid=ssid,
            signal_level=signal_level,
            health_score=health_score,
            signal_rank=signal_rank,
            wifi_mode=wifi_mode,
            ap_name=ap_name,
            ap_mac=ap_mac,
            radio_id=radio_id,
            channel=channel,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            power_save=power_save,
            rssi=rssi,
            snr=snr,
            switch_mac=switch_mac,
            switch_name=switch_name,
            gateway_mac=gateway_mac,
            gateway_name=gateway_name,
            vid=vid,
            network_name=network_name,
            dot_1_x_identity=dot_1_x_identity,
            dot_1_x_vlan=dot_1_x_vlan,
            port=port,
            lag_id=lag_id,
            activity=activity,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            uptime=uptime,
            last_seen=last_seen,
            auth_status=auth_status,
            blocked=blocked,
            guest=guest,
            active=active,
            manager=manager,
            ip_setting=ip_setting,
            down_packet=down_packet,
            up_packet=up_packet,
            rate_limit=rate_limit,
            client_lock_to_ap_setting=client_lock_to_ap_setting,
            support5g2=support5g2,
            multi_link=multi_link,
            unit=unit,
            standard_port=standard_port,
        )

        client_info.additional_properties = d
        return client_info

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
