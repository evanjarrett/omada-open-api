from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_controller_role_vo import ModifyControllerRoleVO
from ...models.operation_response_create_role_result_vo import OperationResponseCreateRoleResultVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    json_body: ModifyControllerRoleVO,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/roles".format(
            omadacId=omadac_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseCreateRoleResultVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseCreateRoleResultVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseCreateRoleResultVO]:
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
    json_body: ModifyControllerRoleVO,
) -> Response[OperationResponseCreateRoleResultVO]:
    """Create new role

     Create new role. Only user with all permissions modify can use this interface.<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30156  -  This role already exists.<br/>-30158  -  An error occurred while creating the
    role.<br/>-30161  -  The number of roles has reached the limit.

    Args:
        omadac_id (str):
        json_body (ModifyControllerRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreateRoleResultVO]
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
    json_body: ModifyControllerRoleVO,
) -> Optional[OperationResponseCreateRoleResultVO]:
    """Create new role

     Create new role. Only user with all permissions modify can use this interface.<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30156  -  This role already exists.<br/>-30158  -  An error occurred while creating the
    role.<br/>-30161  -  The number of roles has reached the limit.

    Args:
        omadac_id (str):
        json_body (ModifyControllerRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreateRoleResultVO
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
    json_body: ModifyControllerRoleVO,
) -> Response[OperationResponseCreateRoleResultVO]:
    """Create new role

     Create new role. Only user with all permissions modify can use this interface.<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30156  -  This role already exists.<br/>-30158  -  An error occurred while creating the
    role.<br/>-30161  -  The number of roles has reached the limit.

    Args:
        omadac_id (str):
        json_body (ModifyControllerRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCreateRoleResultVO]
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
    json_body: ModifyControllerRoleVO,
) -> Optional[OperationResponseCreateRoleResultVO]:
    """Create new role

     Create new role. Only user with all permissions modify can use this interface.<br/><br/>The
    interface requires one of the permissions: <br/>ROLES_WRITE<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30156  -  This role already exists.<br/>-30158  -  An error occurred while creating the
    role.<br/>-30161  -  The number of roles has reached the limit.

    Args:
        omadac_id (str):
        json_body (ModifyControllerRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCreateRoleResultVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
