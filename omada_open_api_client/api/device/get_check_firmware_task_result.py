from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_check_firmware_res import OperationResponseCheckFirmwareRes
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    task_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/all-devices/check-latest-firmware-tasks/{taskId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            taskId=task_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseCheckFirmwareRes]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseCheckFirmwareRes.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseCheckFirmwareRes]:
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
) -> Response[OperationResponseCheckFirmwareRes]:
    """Get the result of the given check latest firmware task

     Get the result of the firmware update task, containing a list of devices with firmware
    updates<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCheckFirmwareRes]
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
) -> Optional[OperationResponseCheckFirmwareRes]:
    """Get the result of the given check latest firmware task

     Get the result of the firmware update task, containing a list of devices with firmware
    updates<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCheckFirmwareRes
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
) -> Response[OperationResponseCheckFirmwareRes]:
    """Get the result of the given check latest firmware task

     Get the result of the firmware update task, containing a list of devices with firmware
    updates<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseCheckFirmwareRes]
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
) -> Optional[OperationResponseCheckFirmwareRes]:
    """Get the result of the given check latest firmware task

     Get the result of the firmware update task, containing a list of devices with firmware
    updates<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseCheckFirmwareRes
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            task_id=task_id,
            client=client,
        )
    ).parsed
