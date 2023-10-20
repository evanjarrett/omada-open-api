from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_local_user_open_api_vo import OperationResponseLocalUserOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/localusers/{id}".format(
            omadacId=omadac_id,
            siteId=site_id,
            id=id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseLocalUserOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseLocalUserOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseLocalUserOpenApiVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseLocalUserOpenApiVO]:
    """Get a local user for given localuserId

     Get a local user with the given omadacId, siteId, local user id.<br/><br/>The interface requires one
    of the permissions: <br/>HOTSPOT_READ<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseLocalUserOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseLocalUserOpenApiVO]:
    """Get a local user for given localuserId

     Get a local user with the given omadacId, siteId, local user id.<br/><br/>The interface requires one
    of the permissions: <br/>HOTSPOT_READ<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseLocalUserOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseLocalUserOpenApiVO]:
    """Get a local user for given localuserId

     Get a local user with the given omadacId, siteId, local user id.<br/><br/>The interface requires one
    of the permissions: <br/>HOTSPOT_READ<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseLocalUserOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseLocalUserOpenApiVO]:
    """Get a local user for given localuserId

     Get a local user with the given omadacId, siteId, local user id.<br/><br/>The interface requires one
    of the permissions: <br/>HOTSPOT_READ<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseLocalUserOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            id=id,
            client=client,
        )
    ).parsed
