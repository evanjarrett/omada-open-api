from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_object import OperationResponseObject
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    role_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/openapi/v1/{omadacId}/roles/{roleId}".format(
            omadacId=omadac_id,
            roleId=role_id,
        ),
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
    role_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseObject]:
    """Delete an existing role

     Delete an existing role. Only user with all permissions modify can use this interface<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30102  -  This role does not exist.<br/>-30153  -  The default role cannot be
    deleted.<br/>-30154  -  An error occurred while deleting the role.<br/>-30155  -  The role cannot be
    deleted since someone has bound to it.<br/>-30173  -  The SSO bound role cannot be deleted!

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        role_id=role_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    role_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseObject]:
    """Delete an existing role

     Delete an existing role. Only user with all permissions modify can use this interface<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30102  -  This role does not exist.<br/>-30153  -  The default role cannot be
    deleted.<br/>-30154  -  An error occurred while deleting the role.<br/>-30155  -  The role cannot be
    deleted since someone has bound to it.<br/>-30173  -  The SSO bound role cannot be deleted!

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return sync_detailed(
        omadac_id=omadac_id,
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    role_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseObject]:
    """Delete an existing role

     Delete an existing role. Only user with all permissions modify can use this interface<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30102  -  This role does not exist.<br/>-30153  -  The default role cannot be
    deleted.<br/>-30154  -  An error occurred while deleting the role.<br/>-30155  -  The role cannot be
    deleted since someone has bound to it.<br/>-30173  -  The SSO bound role cannot be deleted!

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        role_id=role_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    role_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseObject]:
    """Delete an existing role

     Delete an existing role. Only user with all permissions modify can use this interface<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30102  -  This role does not exist.<br/>-30153  -  The default role cannot be
    deleted.<br/>-30154  -  An error occurred while deleting the role.<br/>-30155  -  The role cannot be
    deleted since someone has bound to it.<br/>-30173  -  The SSO bound role cannot be deleted!

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            role_id=role_id,
            client=client,
        )
    ).parsed
