from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_list_controller_role_detail_vo import OperationResponseListControllerRoleDetailVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/roles".format(
            omadacId=omadac_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseListControllerRoleDetailVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseListControllerRoleDetailVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseListControllerRoleDetailVO]:
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
) -> Response[OperationResponseListControllerRoleDetailVO]:
    """Get role list

     Get role list<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListControllerRoleDetailVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseListControllerRoleDetailVO]:
    """Get role list

     Get role list<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListControllerRoleDetailVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseListControllerRoleDetailVO]:
    """Get role list

     Get role list<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListControllerRoleDetailVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseListControllerRoleDetailVO]:
    """Get role list

     Get role list<br/><br/>The interface requires one of the permissions: <br/>ROLES_READ

    Args:
        omadac_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListControllerRoleDetailVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
        )
    ).parsed
