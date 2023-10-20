from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_without_result import OperationResponseWithoutResult
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    task_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/multi-devices/rolling-upgrade-tasks/{taskId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            taskId=task_id,
        ),
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
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """End the rolling upgrade task

     Cancel the rolling upgrade task in the site. But the devices which have complete the upgrade will
    not be rolled back to the old version<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """End the rolling upgrade task

     Cancel the rolling upgrade task in the site. But the devices which have complete the upgrade will
    not be rolled back to the old version<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """End the rolling upgrade task

     Cancel the rolling upgrade task in the site. But the devices which have complete the upgrade will
    not be rolled back to the old version<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """End the rolling upgrade task

     Cancel the rolling upgrade task in the site. But the devices which have complete the upgrade will
    not be rolled back to the old version<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

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
            task_id=task_id,
            client=client,
        )
    ).parsed
