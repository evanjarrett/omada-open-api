from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_task_id import OperationResponseTaskId
from ...models.rolling_upgrade_request_info import RollingUpgradeRequestInfo
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    json_body: RollingUpgradeRequestInfo,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/multi-devices/start-rolling-upgrade".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "json": json_json_body,
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
    json_body: RollingUpgradeRequestInfo,
) -> Response[OperationResponseTaskId]:
    """Start batch rolling upgrade

     Batch online upgrade the devices in a certain order in the site. It is suggested to check firmware
    update before the operation, or the firmware might not be the latest<br/><br/>The interface requires
    one of the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (RollingUpgradeRequestInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseTaskId]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        json_body=json_body,
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
    json_body: RollingUpgradeRequestInfo,
) -> Optional[OperationResponseTaskId]:
    """Start batch rolling upgrade

     Batch online upgrade the devices in a certain order in the site. It is suggested to check firmware
    update before the operation, or the firmware might not be the latest<br/><br/>The interface requires
    one of the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (RollingUpgradeRequestInfo):

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
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: RollingUpgradeRequestInfo,
) -> Response[OperationResponseTaskId]:
    """Start batch rolling upgrade

     Batch online upgrade the devices in a certain order in the site. It is suggested to check firmware
    update before the operation, or the firmware might not be the latest<br/><br/>The interface requires
    one of the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (RollingUpgradeRequestInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseTaskId]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: RollingUpgradeRequestInfo,
) -> Optional[OperationResponseTaskId]:
    """Start batch rolling upgrade

     Batch online upgrade the devices in a certain order in the site. It is suggested to check firmware
    update before the operation, or the firmware might not be the latest<br/><br/>The interface requires
    one of the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (RollingUpgradeRequestInfo):

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
            json_body=json_body,
        )
    ).parsed
