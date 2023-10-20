from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_client_info import OperationResponseClientInfo
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    client_mac: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/clients/{clientMac}".format(
            omadacId=omadac_id,
            siteId=site_id,
            clientMac=client_mac,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseClientInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseClientInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseClientInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseClientInfo]:
    """Get client info

     Get client info.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseClientInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        client_mac=client_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseClientInfo]:
    """Get client info

     Get client info.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseClientInfo
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client_mac=client_mac,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseClientInfo]:
    """Get client info

     Get client info.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseClientInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        client_mac=client_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseClientInfo]:
    """Get client info

     Get client info.<br/><br/>The interface requires one of the permissions:
    <br/>CLIENTS_READ<br/>DEVICES_READ

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseClientInfo
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client_mac=client_mac,
            client=client,
        )
    ).parsed
