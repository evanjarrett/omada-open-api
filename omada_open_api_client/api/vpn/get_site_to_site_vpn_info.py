from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_site_to_site_vpn_entity import OperationResponseSiteToSiteVPNEntity
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/vpn/site-to-site-vpns/{vpnId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            vpnId=vpn_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseSiteToSiteVPNEntity]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseSiteToSiteVPNEntity.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseSiteToSiteVPNEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseSiteToSiteVPNEntity]:
    """Get site-to-site VPN info

     Get site-to-site VPN info.<br/><br/>The interface requires one of the permissions: <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseSiteToSiteVPNEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vpn_id=vpn_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseSiteToSiteVPNEntity]:
    """Get site-to-site VPN info

     Get site-to-site VPN info.<br/><br/>The interface requires one of the permissions: <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseSiteToSiteVPNEntity
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        vpn_id=vpn_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseSiteToSiteVPNEntity]:
    """Get site-to-site VPN info

     Get site-to-site VPN info.<br/><br/>The interface requires one of the permissions: <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseSiteToSiteVPNEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vpn_id=vpn_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseSiteToSiteVPNEntity]:
    """Get site-to-site VPN info

     Get site-to-site VPN info.<br/><br/>The interface requires one of the permissions: <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseSiteToSiteVPNEntity
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            vpn_id=vpn_id,
            client=client,
        )
    ).parsed
