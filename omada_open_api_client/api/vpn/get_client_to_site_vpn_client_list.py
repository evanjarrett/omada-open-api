from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_list_client_to_site_vpn_client_entity import (
    OperationResponseListClientToSiteVPNClientEntity,
)
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/vpn/client-to-site-vpn-clients".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseListClientToSiteVPNClientEntity]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseListClientToSiteVPNClientEntity.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseListClientToSiteVPNClientEntity]:
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
) -> Response[OperationResponseListClientToSiteVPNClientEntity]:
    """Get client-to-site VPN client list

     Get client-to-site VPN client list.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListClientToSiteVPNClientEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
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
) -> Optional[OperationResponseListClientToSiteVPNClientEntity]:
    """Get client-to-site VPN client list

     Get client-to-site VPN client list.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListClientToSiteVPNClientEntity
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseListClientToSiteVPNClientEntity]:
    """Get client-to-site VPN client list

     Get client-to-site VPN client list.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListClientToSiteVPNClientEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseListClientToSiteVPNClientEntity]:
    """Get client-to-site VPN client list

     Get client-to-site VPN client list.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListClientToSiteVPNClientEntity
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
        )
    ).parsed
