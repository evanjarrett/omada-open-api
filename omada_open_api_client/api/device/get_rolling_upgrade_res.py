from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_rolling_upgrade_res import OperationResponseRollingUpgradeRes
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    task_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/multi-devices/rolling-upgrade-tasks/{taskId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            taskId=task_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseRollingUpgradeRes]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseRollingUpgradeRes.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseRollingUpgradeRes]:
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
) -> Response[OperationResponseRollingUpgradeRes]:
    """Get the result of the given rolling upgrade task

     Get the result of the rolling upgrade task. The results include whether the task is finished and how
    many devices have not completed the upgrade.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseRollingUpgradeRes]
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
) -> Optional[OperationResponseRollingUpgradeRes]:
    """Get the result of the given rolling upgrade task

     Get the result of the rolling upgrade task. The results include whether the task is finished and how
    many devices have not completed the upgrade.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseRollingUpgradeRes
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
) -> Response[OperationResponseRollingUpgradeRes]:
    """Get the result of the given rolling upgrade task

     Get the result of the rolling upgrade task. The results include whether the task is finished and how
    many devices have not completed the upgrade.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseRollingUpgradeRes]
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
) -> Optional[OperationResponseRollingUpgradeRes]:
    """Get the result of the given rolling upgrade task

     Get the result of the rolling upgrade task. The results include whether the task is finished and how
    many devices have not completed the upgrade.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseRollingUpgradeRes
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            task_id=task_id,
            client=client,
        )
    ).parsed
