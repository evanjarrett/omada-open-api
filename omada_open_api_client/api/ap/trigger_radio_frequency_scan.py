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
    ap_mac: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/aps/{apMac}/start-rf-scan".format(
            omadacId=omadac_id,
            siteId=site_id,
            apMac=ap_mac,
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
    ap_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    Optimizing WLAN... Please wait.<br/>-34808  -  This AP is not connected.<br/>-34809  -  This AP does
    not support RF Scanning.<br/>-34810  -  Mesh APs do not support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    Optimizing WLAN... Please wait.<br/>-34808  -  This AP is not connected.<br/>-34809  -  This AP does
    not support RF Scanning.<br/>-34810  -  Mesh APs do not support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    Optimizing WLAN... Please wait.<br/>-34808  -  This AP is not connected.<br/>-34809  -  This AP does
    not support RF Scanning.<br/>-34810  -  Mesh APs do not support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning.<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    Optimizing WLAN... Please wait.<br/>-34808  -  This AP is not connected.<br/>-34809  -  This AP does
    not support RF Scanning.<br/>-34810  -  Mesh APs do not support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

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
            ap_mac=ap_mac,
            client=client,
        )
    ).parsed
