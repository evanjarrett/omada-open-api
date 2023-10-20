from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_grid_vosslvpn_resource_group_entity import (
    OperationResponseGridVOSSLVPNResourceGroupEntity,
)
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
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/vpn/ssl-vpn-server/resource-groups".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGridVOSSLVPNResourceGroupEntity]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGridVOSSLVPNResourceGroupEntity.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGridVOSSLVPNResourceGroupEntity]:
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
) -> Response[OperationResponseGridVOSSLVPNResourceGroupEntity]:
    """Get resource group list for SSL VPN server

     Get resource group list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSSLVPNResourceGroupEntity]
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
) -> Optional[OperationResponseGridVOSSLVPNResourceGroupEntity]:
    """Get resource group list for SSL VPN server

     Get resource group list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSSLVPNResourceGroupEntity
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
) -> Response[OperationResponseGridVOSSLVPNResourceGroupEntity]:
    """Get resource group list for SSL VPN server

     Get resource group list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSSLVPNResourceGroupEntity]
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
) -> Optional[OperationResponseGridVOSSLVPNResourceGroupEntity]:
    """Get resource group list for SSL VPN server

     Get resource group list for SSL VPN server.<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSSLVPNResourceGroupEntity
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
