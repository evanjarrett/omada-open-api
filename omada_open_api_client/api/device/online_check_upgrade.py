from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_task_id import OperationResponseTaskId
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/all-devices/start-check-latest-firmware".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseTaskId]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseTaskId.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseTaskId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseTaskId]:
    """Start check latest firmware for all devices

     Start a task to query the latest firmware of all devices in the cloud.<br/><br/>The interface
    requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseTaskId]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseTaskId]:
    """Start check latest firmware for all devices

     Start a task to query the latest firmware of all devices in the cloud.<br/><br/>The interface
    requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseTaskId
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseTaskId]:
    """Start check latest firmware for all devices

     Start a task to query the latest firmware of all devices in the cloud.<br/><br/>The interface
    requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseTaskId]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseTaskId]:
    """Start check latest firmware for all devices

     Start a task to query the latest firmware of all devices in the cloud.<br/><br/>The interface
    requires one of the permissions: <br/>DEVICES_WRITE

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseTaskId
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
        )
    ).parsed
