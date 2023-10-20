from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_vo import DeleteUserVO
from ...models.operation_response_object import OperationResponseObject
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    user_id: str,
    *,
    json_body: DeleteUserVO,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
        "url": "/openapi/v1/{omadacId}/users/{userID}".format(
            omadacId=omadac_id,
            userID=user_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseObject]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseObject.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeleteUserVO,
) -> Response[OperationResponseObject]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30112  -  This user does
    not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -  Are you sure you
    want to delete Administrator %Username%? When it is deleted, the viewer accounts it has created will
    be moved to your account.<br/>-44118  -  This interface only supports the authorization code mode,
    not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        user_id=user_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeleteUserVO,
) -> Optional[OperationResponseObject]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30112  -  This user does
    not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -  Are you sure you
    want to delete Administrator %Username%? When it is deleted, the viewer accounts it has created will
    be moved to your account.<br/>-44118  -  This interface only supports the authorization code mode,
    not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return sync_detailed(
        omadac_id=omadac_id,
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeleteUserVO,
) -> Response[OperationResponseObject]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30112  -  This user does
    not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -  Are you sure you
    want to delete Administrator %Username%? When it is deleted, the viewer accounts it has created will
    be moved to your account.<br/>-44118  -  This interface only supports the authorization code mode,
    not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        user_id=user_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeleteUserVO,
) -> Optional[OperationResponseObject]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30112  -  This user does
    not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -  Are you sure you
    want to delete Administrator %Username%? When it is deleted, the viewer accounts it has created will
    be moved to your account.<br/>-44118  -  This interface only supports the authorization code mode,
    not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
