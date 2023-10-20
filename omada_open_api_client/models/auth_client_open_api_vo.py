from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthClientOpenApiVO")


@_attrs_define
class AuthClientOpenApiVO:
    """
    Attributes:
        id (Union[Unset, str]): AuthRecord ID
        name (Union[Unset, str]): Client name
        mac (Union[Unset, str]): Client mac
        wireless (Union[Unset, bool]): Is it wireless type
        ssid (Union[Unset, str]): SSID name
        network_name (Union[Unset, str]): Network name
        auth_type (Union[Unset, int]): Auth type

            0: No Auth 1: Simple Password 2: Exrternal Radius 3: Voucher

            4: External Portal Server 5: Local User 6: SMS 7: Facebook

            8: Hotspot Radius 9: Mac Auth (with fail over) 10: Admin auth 12：form auth
        fb_ver (Union[Unset, int]): Version of Facebook Wi-Fi (authType = Facebook or Facebook V2)
        download (Union[Unset, int]): Total Download (Byte)
        upload (Union[Unset, int]): Total Upload (Byte)
        duration (Union[Unset, int]): Total Duration (s)
        start (Union[Unset, int]): Start timestamp
        end (Union[Unset, int]): End timestamp
        valid (Union[Unset, bool]): Is the client valid
        local_user_name (Union[Unset, str]): LocalUser Name (authType = Local User)
        voucher_code (Union[Unset, str]): Voucher code (authType = Voucher)
        form_name (Union[Unset, str]): form name (authType = form auth)
        radius_username (Union[Unset, str]): Radius userName (authType = External RADIUS or Hotspot RADIUS)
        admin_name (Union[Unset, str]): Admin name (authType = ADMIN)
        ip (Union[Unset, str]): IP address at the time of authentication
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    wireless: Union[Unset, bool] = UNSET
    ssid: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    auth_type: Union[Unset, int] = UNSET
    fb_ver: Union[Unset, int] = UNSET
    download: Union[Unset, int] = UNSET
    upload: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    start: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET
    valid: Union[Unset, bool] = UNSET
    local_user_name: Union[Unset, str] = UNSET
    voucher_code: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    radius_username: Union[Unset, str] = UNSET
    admin_name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        mac = self.mac
        wireless = self.wireless
        ssid = self.ssid
        network_name = self.network_name
        auth_type = self.auth_type
        fb_ver = self.fb_ver
        download = self.download
        upload = self.upload
        duration = self.duration
        start = self.start
        end = self.end
        valid = self.valid
        local_user_name = self.local_user_name
        voucher_code = self.voucher_code
        form_name = self.form_name
        radius_username = self.radius_username
        admin_name = self.admin_name
        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if fb_ver is not UNSET:
            field_dict["fbVer"] = fb_ver
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if duration is not UNSET:
            field_dict["duration"] = duration
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if valid is not UNSET:
            field_dict["valid"] = valid
        if local_user_name is not UNSET:
            field_dict["localUserName"] = local_user_name
        if voucher_code is not UNSET:
            field_dict["voucherCode"] = voucher_code
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if radius_username is not UNSET:
            field_dict["radiusUsername"] = radius_username
        if admin_name is not UNSET:
            field_dict["adminName"] = admin_name
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        wireless = d.pop("wireless", UNSET)

        ssid = d.pop("ssid", UNSET)

        network_name = d.pop("networkName", UNSET)

        auth_type = d.pop("authType", UNSET)

        fb_ver = d.pop("fbVer", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        duration = d.pop("duration", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        valid = d.pop("valid", UNSET)

        local_user_name = d.pop("localUserName", UNSET)

        voucher_code = d.pop("voucherCode", UNSET)

        form_name = d.pop("formName", UNSET)

        radius_username = d.pop("radiusUsername", UNSET)

        admin_name = d.pop("adminName", UNSET)

        ip = d.pop("ip", UNSET)

        auth_client_open_api_vo = cls(
            id=id,
            name=name,
            mac=mac,
            wireless=wireless,
            ssid=ssid,
            network_name=network_name,
            auth_type=auth_type,
            fb_ver=fb_ver,
            download=download,
            upload=upload,
            duration=duration,
            start=start,
            end=end,
            valid=valid,
            local_user_name=local_user_name,
            voucher_code=voucher_code,
            form_name=form_name,
            radius_username=radius_username,
            admin_name=admin_name,
            ip=ip,
        )

        auth_client_open_api_vo.additional_properties = d
        return auth_client_open_api_vo

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
