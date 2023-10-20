from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_list_dashboard_vpn_stats import OperationResponseListDashboardVpnStats
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    type: int,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/dashboard/vpn-tunnel-stats".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseListDashboardVpnStats]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseListDashboardVpnStats.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseListDashboardVpnStats]:
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
    type: int,
) -> Response[OperationResponseListDashboardVpnStats]:
    """Get grid dashboard tunnel statistic list

     Get the status, IP address, and other information of the established dashboard tunnel statistic VPN
    connection<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        type (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListDashboardVpnStats]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        type=type,
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
    type: int,
) -> Optional[OperationResponseListDashboardVpnStats]:
    """Get grid dashboard tunnel statistic list

     Get the status, IP address, and other information of the established dashboard tunnel statistic VPN
    connection<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        type (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListDashboardVpnStats
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: int,
) -> Response[OperationResponseListDashboardVpnStats]:
    """Get grid dashboard tunnel statistic list

     Get the status, IP address, and other information of the established dashboard tunnel statistic VPN
    connection<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        type (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListDashboardVpnStats]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: int,
) -> Optional[OperationResponseListDashboardVpnStats]:
    """Get grid dashboard tunnel statistic list

     Get the status, IP address, and other information of the established dashboard tunnel statistic VPN
    connection<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        type (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListDashboardVpnStats
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            type=type,
        )
    ).parsed
