from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_site_settingremote_logging import OperationResponseSiteSettingremoteLogging
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/remote-logging".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseSiteSettingremoteLogging]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseSiteSettingremoteLogging.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseSiteSettingremoteLogging]:
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
) -> Response[OperationResponseSiteSettingremoteLogging]:
    """Get site remote logging setting

     Get site remote logging setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/>MAP_READ<br/>HOTSPOT_READ<br/>DEVICES_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1300  -  Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseSiteSettingremoteLogging]
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
) -> Optional[OperationResponseSiteSettingremoteLogging]:
    """Get site remote logging setting

     Get site remote logging setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/>MAP_READ<br/>HOTSPOT_READ<br/>DEVICES_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1300  -  Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseSiteSettingremoteLogging
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
) -> Response[OperationResponseSiteSettingremoteLogging]:
    """Get site remote logging setting

     Get site remote logging setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/>MAP_READ<br/>HOTSPOT_READ<br/>DEVICES_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1300  -  Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseSiteSettingremoteLogging]
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
) -> Optional[OperationResponseSiteSettingremoteLogging]:
    """Get site remote logging setting

     Get site remote logging setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_READ<br/>MAP_READ<br/>HOTSPOT_READ<br/>DEVICES_READ<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-1300  -  Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseSiteSettingremoteLogging
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
        )
    ).parsed
