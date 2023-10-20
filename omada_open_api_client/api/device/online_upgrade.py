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
    device_mac: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/devices/{deviceMac}/start-online-upgrade".format(
            omadacId=omadac_id,
            siteId=site_id,
            deviceMac=device_mac,
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
    device_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Start online upgrade

     Upgrade the device with the latest firmware in the cloud. It is suggested to check firmware update
    before the operation, or the firmware might not be the latest<br/><br/>The interface requires one of
    the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.<br/>-39026  -  The upgrade file is the same
    with the current version.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """Start online upgrade

     Upgrade the device with the latest firmware in the cloud. It is suggested to check firmware update
    before the operation, or the firmware might not be the latest<br/><br/>The interface requires one of
    the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.<br/>-39026  -  The upgrade file is the same
    with the current version.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Start online upgrade

     Upgrade the device with the latest firmware in the cloud. It is suggested to check firmware update
    before the operation, or the firmware might not be the latest<br/><br/>The interface requires one of
    the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.<br/>-39026  -  The upgrade file is the same
    with the current version.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """Start online upgrade

     Upgrade the device with the latest firmware in the cloud. It is suggested to check firmware update
    before the operation, or the firmware might not be the latest<br/><br/>The interface requires one of
    the permissions: <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-39020  -  Failed
    to upgrade because no device is ready for upgrading.<br/>-39026  -  The upgrade file is the same
    with the current version.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):

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
            device_mac=device_mac,
            client=client,
        )
    ).parsed
