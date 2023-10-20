from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_vo import CreateUserVO
from ...models.operation_response_create_user_result_vo import OperationResponseCreateUserResultVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    json_body: CreateUserVO,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/users".format(
            omadacId=omadac_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseCreateUserResultVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseCreateUserResultVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseCreateUserResultVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateUserVO,
) -> Response[OperationResponseCreateUserResultVO]:
    """Create new user

     Create new user. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30124  -  The number of users has reached the limit.<br/>-44118
    -  This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        omadac_id (str):
        json_body (CreateUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreateUserResultVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateUserVO,
) -> Optional[OperationResponseCreateUserResultVO]:
    """Create new user

     Create new user. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30124  -  The number of users has reached the limit.<br/>-44118
    -  This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        omadac_id (str):
        json_body (CreateUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreateUserResultVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateUserVO,
) -> Response[OperationResponseCreateUserResultVO]:
    """Create new user

     Create new user. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30124  -  The number of users has reached the limit.<br/>-44118
    -  This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        omadac_id (str):
        json_body (CreateUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreateUserResultVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateUserVO,
) -> Optional[OperationResponseCreateUserResultVO]:
    """Create new user

     Create new user. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30124  -  The number of users has reached the limit.<br/>-44118
    -  This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        omadac_id (str):
        json_body (CreateUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreateUserResultVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
