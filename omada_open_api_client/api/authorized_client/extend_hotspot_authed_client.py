from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extend_time_entity import ExtendTimeEntity
from ...models.operation_response_without_result import OperationResponseWithoutResult
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    json_body: ExtendTimeEntity,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/authed-records/{id}/period".format(
            omadacId=omadac_id,
            siteId=site_id,
            id=id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseWithoutResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseWithoutResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseWithoutResult]:
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
    json_body: ExtendTimeEntity,
) -> Response[OperationResponseWithoutResult]:
    """Modify period for given authed record

     Extend the valid time of the authentication record with the given omadacId, siteId,
    authClientId.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-1005  -  Operation forbidden.<br/>-1200
    -  You have been logged out of the controller. This may have been caused by data restore, reboot,
    session timeout or disabled cloud access. Please try to log in again later.<br/>-44111  -  The Grant
    Type is Invalid.<br/>-44112  -  The Access Token has expired.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        json_body (ExtendTimeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        json_body=json_body,
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
    json_body: ExtendTimeEntity,
) -> Optional[OperationResponseWithoutResult]:
    """Modify period for given authed record

     Extend the valid time of the authentication record with the given omadacId, siteId,
    authClientId.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-1005  -  Operation forbidden.<br/>-1200
    -  You have been logged out of the controller. This may have been caused by data restore, reboot,
    session timeout or disabled cloud access. Please try to log in again later.<br/>-44111  -  The Grant
    Type is Invalid.<br/>-44112  -  The Access Token has expired.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        json_body (ExtendTimeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtendTimeEntity,
) -> Response[OperationResponseWithoutResult]:
    """Modify period for given authed record

     Extend the valid time of the authentication record with the given omadacId, siteId,
    authClientId.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-1005  -  Operation forbidden.<br/>-1200
    -  You have been logged out of the controller. This may have been caused by data restore, reboot,
    session timeout or disabled cloud access. Please try to log in again later.<br/>-44111  -  The Grant
    Type is Invalid.<br/>-44112  -  The Access Token has expired.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        json_body (ExtendTimeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtendTimeEntity,
) -> Optional[OperationResponseWithoutResult]:
    """Modify period for given authed record

     Extend the valid time of the authentication record with the given omadacId, siteId,
    authClientId.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-1005  -  Operation forbidden.<br/>-1200
    -  You have been logged out of the controller. This may have been caused by data restore, reboot,
    session timeout or disabled cloud access. Please try to log in again later.<br/>-44111  -  The Grant
    Type is Invalid.<br/>-44112  -  The Access Token has expired.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        json_body (ExtendTimeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
