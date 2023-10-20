from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_grid_vo_auth_client_open_api_vo import OperationResponseGridVOAuthClientOpenApiVO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_mac: Union[Unset, None, str] = UNSET,
    sorts_ip: Union[Unset, None, str] = UNSET,
    sorts_auth_type: Union[Unset, None, str] = UNSET,
    sorts_ssid_or_network: Union[Unset, None, str] = UNSET,
    sorts_download: Union[Unset, None, str] = UNSET,
    sorts_upload: Union[Unset, None, str] = UNSET,
    sorts_status: Union[Unset, None, str] = UNSET,
    sorts_start: Union[Unset, None, str] = UNSET,
    sorts_end: Union[Unset, None, str] = UNSET,
    sorts_duration: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["sorts.mac"] = sorts_mac

    params["sorts.ip"] = sorts_ip

    params["sorts.authType"] = sorts_auth_type

    params["sorts.ssidOrNetwork"] = sorts_ssid_or_network

    params["sorts.download"] = sorts_download

    params["sorts.upload"] = sorts_upload

    params["sorts.status"] = sorts_status

    params["sorts.start"] = sorts_start

    params["sorts.end"] = sorts_end

    params["sorts.duration"] = sorts_duration

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/authed-records".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGridVOAuthClientOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGridVOAuthClientOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGridVOAuthClientOpenApiVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_mac: Union[Unset, None, str] = UNSET,
    sorts_ip: Union[Unset, None, str] = UNSET,
    sorts_auth_type: Union[Unset, None, str] = UNSET,
    sorts_ssid_or_network: Union[Unset, None, str] = UNSET,
    sorts_download: Union[Unset, None, str] = UNSET,
    sorts_upload: Union[Unset, None, str] = UNSET,
    sorts_status: Union[Unset, None, str] = UNSET,
    sorts_start: Union[Unset, None, str] = UNSET,
    sorts_end: Union[Unset, None, str] = UNSET,
    sorts_duration: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOAuthClientOpenApiVO]:
    """Get authentication record list

     Get all authentication records in a site with the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ<br/>INSIGHT_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1005  -  Operation forbidden.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        sorts_auth_type (Union[Unset, None, str]):
        sorts_ssid_or_network (Union[Unset, None, str]):
        sorts_download (Union[Unset, None, str]):
        sorts_upload (Union[Unset, None, str]):
        sorts_status (Union[Unset, None, str]):
        sorts_start (Union[Unset, None, str]):
        sorts_end (Union[Unset, None, str]):
        sorts_duration (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOAuthClientOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_auth_type=sorts_auth_type,
        sorts_ssid_or_network=sorts_ssid_or_network,
        sorts_download=sorts_download,
        sorts_upload=sorts_upload,
        sorts_status=sorts_status,
        sorts_start=sorts_start,
        sorts_end=sorts_end,
        sorts_duration=sorts_duration,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_mac: Union[Unset, None, str] = UNSET,
    sorts_ip: Union[Unset, None, str] = UNSET,
    sorts_auth_type: Union[Unset, None, str] = UNSET,
    sorts_ssid_or_network: Union[Unset, None, str] = UNSET,
    sorts_download: Union[Unset, None, str] = UNSET,
    sorts_upload: Union[Unset, None, str] = UNSET,
    sorts_status: Union[Unset, None, str] = UNSET,
    sorts_start: Union[Unset, None, str] = UNSET,
    sorts_end: Union[Unset, None, str] = UNSET,
    sorts_duration: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOAuthClientOpenApiVO]:
    """Get authentication record list

     Get all authentication records in a site with the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ<br/>INSIGHT_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1005  -  Operation forbidden.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        sorts_auth_type (Union[Unset, None, str]):
        sorts_ssid_or_network (Union[Unset, None, str]):
        sorts_download (Union[Unset, None, str]):
        sorts_upload (Union[Unset, None, str]):
        sorts_status (Union[Unset, None, str]):
        sorts_start (Union[Unset, None, str]):
        sorts_end (Union[Unset, None, str]):
        sorts_duration (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOAuthClientOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_auth_type=sorts_auth_type,
        sorts_ssid_or_network=sorts_ssid_or_network,
        sorts_download=sorts_download,
        sorts_upload=sorts_upload,
        sorts_status=sorts_status,
        sorts_start=sorts_start,
        sorts_end=sorts_end,
        sorts_duration=sorts_duration,
        search_key=search_key,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_mac: Union[Unset, None, str] = UNSET,
    sorts_ip: Union[Unset, None, str] = UNSET,
    sorts_auth_type: Union[Unset, None, str] = UNSET,
    sorts_ssid_or_network: Union[Unset, None, str] = UNSET,
    sorts_download: Union[Unset, None, str] = UNSET,
    sorts_upload: Union[Unset, None, str] = UNSET,
    sorts_status: Union[Unset, None, str] = UNSET,
    sorts_start: Union[Unset, None, str] = UNSET,
    sorts_end: Union[Unset, None, str] = UNSET,
    sorts_duration: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOAuthClientOpenApiVO]:
    """Get authentication record list

     Get all authentication records in a site with the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ<br/>INSIGHT_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1005  -  Operation forbidden.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        sorts_auth_type (Union[Unset, None, str]):
        sorts_ssid_or_network (Union[Unset, None, str]):
        sorts_download (Union[Unset, None, str]):
        sorts_upload (Union[Unset, None, str]):
        sorts_status (Union[Unset, None, str]):
        sorts_start (Union[Unset, None, str]):
        sorts_end (Union[Unset, None, str]):
        sorts_duration (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOAuthClientOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_auth_type=sorts_auth_type,
        sorts_ssid_or_network=sorts_ssid_or_network,
        sorts_download=sorts_download,
        sorts_upload=sorts_upload,
        sorts_status=sorts_status,
        sorts_start=sorts_start,
        sorts_end=sorts_end,
        sorts_duration=sorts_duration,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_mac: Union[Unset, None, str] = UNSET,
    sorts_ip: Union[Unset, None, str] = UNSET,
    sorts_auth_type: Union[Unset, None, str] = UNSET,
    sorts_ssid_or_network: Union[Unset, None, str] = UNSET,
    sorts_download: Union[Unset, None, str] = UNSET,
    sorts_upload: Union[Unset, None, str] = UNSET,
    sorts_status: Union[Unset, None, str] = UNSET,
    sorts_start: Union[Unset, None, str] = UNSET,
    sorts_end: Union[Unset, None, str] = UNSET,
    sorts_duration: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOAuthClientOpenApiVO]:
    """Get authentication record list

     Get all authentication records in a site with the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ<br/>INSIGHT_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1005  -  Operation forbidden.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        sorts_auth_type (Union[Unset, None, str]):
        sorts_ssid_or_network (Union[Unset, None, str]):
        sorts_download (Union[Unset, None, str]):
        sorts_upload (Union[Unset, None, str]):
        sorts_status (Union[Unset, None, str]):
        sorts_start (Union[Unset, None, str]):
        sorts_end (Union[Unset, None, str]):
        sorts_duration (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOAuthClientOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            page=page,
            page_size=page_size,
            sorts_name=sorts_name,
            sorts_mac=sorts_mac,
            sorts_ip=sorts_ip,
            sorts_auth_type=sorts_auth_type,
            sorts_ssid_or_network=sorts_ssid_or_network,
            sorts_download=sorts_download,
            sorts_upload=sorts_upload,
            sorts_status=sorts_status,
            sorts_start=sorts_start,
            sorts_end=sorts_end,
            sorts_duration=sorts_duration,
            search_key=search_key,
        )
    ).parsed
