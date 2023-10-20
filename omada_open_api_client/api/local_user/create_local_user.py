from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.local_user_entity import LocalUserEntity
from ...models.operation_response_created_res_id_open_api_vo import OperationResponseCreatedResIdOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    json_body: LocalUserEntity,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/localusers".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseCreatedResIdOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseCreatedResIdOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseCreatedResIdOpenApiVO]:
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
    json_body: LocalUserEntity,
) -> Response[OperationResponseCreatedResIdOpenApiVO]:
    """Create a new local user

     Create a local user with the given params.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-33000  -  This site does not
    exist.<br/>-33004  -  Operation failed because other operations are being performed on this site.
    Please wait and try again later.<br/>-42012  -  The number of local users has reached the limit. New
    local users cannot be created.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (LocalUserEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreatedResIdOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        json_body=json_body,
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
    json_body: LocalUserEntity,
) -> Optional[OperationResponseCreatedResIdOpenApiVO]:
    """Create a new local user

     Create a local user with the given params.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-33000  -  This site does not
    exist.<br/>-33004  -  Operation failed because other operations are being performed on this site.
    Please wait and try again later.<br/>-42012  -  The number of local users has reached the limit. New
    local users cannot be created.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (LocalUserEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreatedResIdOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocalUserEntity,
) -> Response[OperationResponseCreatedResIdOpenApiVO]:
    """Create a new local user

     Create a local user with the given params.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-33000  -  This site does not
    exist.<br/>-33004  -  Operation failed because other operations are being performed on this site.
    Please wait and try again later.<br/>-42012  -  The number of local users has reached the limit. New
    local users cannot be created.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (LocalUserEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreatedResIdOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocalUserEntity,
) -> Optional[OperationResponseCreatedResIdOpenApiVO]:
    """Create a new local user

     Create a local user with the given params.<br/><br/>The interface requires one of the permissions:
    <br/>HOTSPOT_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-33000  -  This site does not
    exist.<br/>-33004  -  Operation failed because other operations are being performed on this site.
    Please wait and try again later.<br/>-42012  -  The number of local users has reached the limit. New
    local users cannot be created.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (LocalUserEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreatedResIdOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
