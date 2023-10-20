from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_user_vo import ModifyUserVO
from ...models.operation_response_object import OperationResponseObject
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    user_id: str,
    *,
    json_body: ModifyUserVO,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
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
    json_body: ModifyUserVO,
) -> Response[OperationResponseObject]:
    """Modify an existing user

     Modify an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30108  -  This username does not exist.<br/>-30133  -  Failed
    to remove Site %Site name%. The administrator account should not have privileges to fewer sites than
    that of the viewer accounts it has created.<br/>-30134  -  Failed to add Site %Site name%. The
    viewer account should not have privileges to more sites thatn that of its immediate superior
    account.<br/>-30135  -  Are you sure you want to change the role of %Username% from Administrator to
    Viewer?If its role is changed, the viewer accounts it has created will be moved to your
    account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (ModifyUserVO):

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
    json_body: ModifyUserVO,
) -> Optional[OperationResponseObject]:
    """Modify an existing user

     Modify an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30108  -  This username does not exist.<br/>-30133  -  Failed
    to remove Site %Site name%. The administrator account should not have privileges to fewer sites than
    that of the viewer accounts it has created.<br/>-30134  -  Failed to add Site %Site name%. The
    viewer account should not have privileges to more sites thatn that of its immediate superior
    account.<br/>-30135  -  Are you sure you want to change the role of %Username% from Administrator to
    Viewer?If its role is changed, the viewer accounts it has created will be moved to your
    account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (ModifyUserVO):

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
    json_body: ModifyUserVO,
) -> Response[OperationResponseObject]:
    """Modify an existing user

     Modify an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30108  -  This username does not exist.<br/>-30133  -  Failed
    to remove Site %Site name%. The administrator account should not have privileges to fewer sites than
    that of the viewer accounts it has created.<br/>-30134  -  Failed to add Site %Site name%. The
    viewer account should not have privileges to more sites thatn that of its immediate superior
    account.<br/>-30135  -  Are you sure you want to change the role of %Username% from Administrator to
    Viewer?If its role is changed, the viewer accounts it has created will be moved to your
    account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (ModifyUserVO):

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
    json_body: ModifyUserVO,
) -> Optional[OperationResponseObject]:
    """Modify an existing user

     Modify an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>USERS_WRITE<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-30103  -  Invalid email
    address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid password.<br/>-30106  -  This
    username is already registered.<br/>-30108  -  This username does not exist.<br/>-30133  -  Failed
    to remove Site %Site name%. The administrator account should not have privileges to fewer sites than
    that of the viewer accounts it has created.<br/>-30134  -  Failed to add Site %Site name%. The
    viewer account should not have privileges to more sites thatn that of its immediate superior
    account.<br/>-30135  -  Are you sure you want to change the role of %Username% from Administrator to
    Viewer?If its role is changed, the viewer accounts it has created will be moved to your
    account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        json_body (ModifyUserVO):

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
