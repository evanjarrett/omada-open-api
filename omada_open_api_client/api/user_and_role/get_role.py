from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_controller_role_detail_vo import OperationResponseControllerRoleDetailVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    role_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/roles/{roleId}".format(
            omadacId=omadac_id,
            roleId=role_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseControllerRoleDetailVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseControllerRoleDetailVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseControllerRoleDetailVO]:
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
) -> Response[OperationResponseControllerRoleDetailVO]:
    """Get role info

     Get role info<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseControllerRoleDetailVO]
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
) -> Optional[OperationResponseControllerRoleDetailVO]:
    """Get role info

     Get role info<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseControllerRoleDetailVO
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
) -> Response[OperationResponseControllerRoleDetailVO]:
    """Get role info

     Get role info<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseControllerRoleDetailVO]
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
) -> Optional[OperationResponseControllerRoleDetailVO]:
    """Get role info

     Get role info<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseControllerRoleDetailVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            role_id=role_id,
            client=client,
        )
    ).parsed
