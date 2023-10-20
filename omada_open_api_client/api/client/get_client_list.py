from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_client_grid_vo_client_info import OperationResponseClientGridVOClientInfo
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
    filters_wireless: Union[Unset, None, str] = UNSET,
    filters_radio_id: Union[Unset, None, str] = UNSET,
    filters_ap_mac: Union[Unset, None, str] = UNSET,
    filters_switch_mac: Union[Unset, None, str] = UNSET,
    filters_gateway_mac: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["sorts.mac"] = sorts_mac

    params["sorts.ip"] = sorts_ip

    params["filters.wireless"] = filters_wireless

    params["filters.radioId"] = filters_radio_id

    params["filters.apMac"] = filters_ap_mac

    params["filters.switchMac"] = filters_switch_mac

    params["filters.gatewayMac"] = filters_gateway_mac

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/clients".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseClientGridVOClientInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseClientGridVOClientInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseClientGridVOClientInfo]:
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
    filters_wireless: Union[Unset, None, str] = UNSET,
    filters_radio_id: Union[Unset, None, str] = UNSET,
    filters_ap_mac: Union[Unset, None, str] = UNSET,
    filters_switch_mac: Union[Unset, None, str] = UNSET,
    filters_gateway_mac: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseClientGridVOClientInfo]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        filters_wireless (Union[Unset, None, str]):
        filters_radio_id (Union[Unset, None, str]):
        filters_ap_mac (Union[Unset, None, str]):
        filters_switch_mac (Union[Unset, None, str]):
        filters_gateway_mac (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseClientGridVOClientInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        filters_wireless=filters_wireless,
        filters_radio_id=filters_radio_id,
        filters_ap_mac=filters_ap_mac,
        filters_switch_mac=filters_switch_mac,
        filters_gateway_mac=filters_gateway_mac,
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
    filters_wireless: Union[Unset, None, str] = UNSET,
    filters_radio_id: Union[Unset, None, str] = UNSET,
    filters_ap_mac: Union[Unset, None, str] = UNSET,
    filters_switch_mac: Union[Unset, None, str] = UNSET,
    filters_gateway_mac: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseClientGridVOClientInfo]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        filters_wireless (Union[Unset, None, str]):
        filters_radio_id (Union[Unset, None, str]):
        filters_ap_mac (Union[Unset, None, str]):
        filters_switch_mac (Union[Unset, None, str]):
        filters_gateway_mac (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseClientGridVOClientInfo
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
        filters_wireless=filters_wireless,
        filters_radio_id=filters_radio_id,
        filters_ap_mac=filters_ap_mac,
        filters_switch_mac=filters_switch_mac,
        filters_gateway_mac=filters_gateway_mac,
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
    filters_wireless: Union[Unset, None, str] = UNSET,
    filters_radio_id: Union[Unset, None, str] = UNSET,
    filters_ap_mac: Union[Unset, None, str] = UNSET,
    filters_switch_mac: Union[Unset, None, str] = UNSET,
    filters_gateway_mac: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseClientGridVOClientInfo]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        filters_wireless (Union[Unset, None, str]):
        filters_radio_id (Union[Unset, None, str]):
        filters_ap_mac (Union[Unset, None, str]):
        filters_switch_mac (Union[Unset, None, str]):
        filters_gateway_mac (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseClientGridVOClientInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        filters_wireless=filters_wireless,
        filters_radio_id=filters_radio_id,
        filters_ap_mac=filters_ap_mac,
        filters_switch_mac=filters_switch_mac,
        filters_gateway_mac=filters_gateway_mac,
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
    filters_wireless: Union[Unset, None, str] = UNSET,
    filters_radio_id: Union[Unset, None, str] = UNSET,
    filters_ap_mac: Union[Unset, None, str] = UNSET,
    filters_switch_mac: Union[Unset, None, str] = UNSET,
    filters_gateway_mac: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseClientGridVOClientInfo]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        sorts_mac (Union[Unset, None, str]):
        sorts_ip (Union[Unset, None, str]):
        filters_wireless (Union[Unset, None, str]):
        filters_radio_id (Union[Unset, None, str]):
        filters_ap_mac (Union[Unset, None, str]):
        filters_switch_mac (Union[Unset, None, str]):
        filters_gateway_mac (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseClientGridVOClientInfo
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
            filters_wireless=filters_wireless,
            filters_radio_id=filters_radio_id,
            filters_ap_mac=filters_ap_mac,
            filters_switch_mac=filters_switch_mac,
            filters_gateway_mac=filters_gateway_mac,
            search_key=search_key,
        )
    ).parsed
