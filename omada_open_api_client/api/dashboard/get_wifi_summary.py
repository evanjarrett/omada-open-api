from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_wifi_summary import OperationResponseWifiSummary
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    start: int,
    end: int,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/dashboard/wifi-summary".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseWifiSummary]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseWifiSummary.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseWifiSummary]:
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
    start: int,
    end: int,
) -> Response[OperationResponseWifiSummary]:
    """Get wifi summary

     Get wifi summary.<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        start (int):
        end (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWifiSummary]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        start=start,
        end=end,
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
    start: int,
    end: int,
) -> Optional[OperationResponseWifiSummary]:
    """Get wifi summary

     Get wifi summary.<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        start (int):
        end (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWifiSummary
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: int,
    end: int,
) -> Response[OperationResponseWifiSummary]:
    """Get wifi summary

     Get wifi summary.<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        start (int):
        end (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWifiSummary]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: int,
    end: int,
) -> Optional[OperationResponseWifiSummary]:
    """Get wifi summary

     Get wifi summary.<br/><br/>The interface requires one of the permissions: <br/>DASHBOARD_READ

    Args:
        omadac_id (str):
        site_id (str):
        start (int):
        end (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWifiSummary
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
