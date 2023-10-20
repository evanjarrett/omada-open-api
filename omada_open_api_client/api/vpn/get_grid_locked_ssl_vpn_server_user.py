from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_grid_vosslvpn_lock_entity import OperationResponseGridVOSSLVPNLockEntity
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    page: int,
    page_size: int,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/vpn/ssl-vpn-server/locked-users".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGridVOSSLVPNLockEntity]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGridVOSSLVPNLockEntity.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGridVOSSLVPNLockEntity]:
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
) -> Response[OperationResponseGridVOSSLVPNLockEntity]:
    """Get locked user list for SSL VPN server

     Get locked user list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-43008  -  The current gateway model or
    firmware version does not support SSL VPN configuration.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSSLVPNLockEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
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
) -> Optional[OperationResponseGridVOSSLVPNLockEntity]:
    """Get locked user list for SSL VPN server

     Get locked user list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-43008  -  The current gateway model or
    firmware version does not support SSL VPN configuration.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSSLVPNLockEntity
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
) -> Response[OperationResponseGridVOSSLVPNLockEntity]:
    """Get locked user list for SSL VPN server

     Get locked user list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-43008  -  The current gateway model or
    firmware version does not support SSL VPN configuration.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSSLVPNLockEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
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
) -> Optional[OperationResponseGridVOSSLVPNLockEntity]:
    """Get locked user list for SSL VPN server

     Get locked user list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-43008  -  The current gateway model or
    firmware version does not support SSL VPN configuration.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSSLVPNLockEntity
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
