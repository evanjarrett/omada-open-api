from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_without_result import OperationResponseWithoutResult
from ...models.update_the_switch_port_poe_entity import UpdateTheSwitchPortPoeEntity
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    json_body: UpdateTheSwitchPortPoeEntity,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/switches/{switchMac}/ports/{port}/poe-mode".format(
            omadacId=omadac_id,
            siteId=site_id,
            switchMac=switch_mac,
            port=port,
        ),
        "json": json_json_body,
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
    switch_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UpdateTheSwitchPortPoeEntity,
) -> Response[OperationResponseWithoutResult]:
    """Set poe mode for given port

     Set poe mode for given port. Please enable profile override first to use this
    interface.<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-39050  -  This device does not exist.<br/>-39701  -  Port does not
    exist<br/>-39737  -  Profile override setting is disabled.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        json_body (UpdateTheSwitchPortPoeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        port=port,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UpdateTheSwitchPortPoeEntity,
) -> Optional[OperationResponseWithoutResult]:
    """Set poe mode for given port

     Set poe mode for given port. Please enable profile override first to use this
    interface.<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-39050  -  This device does not exist.<br/>-39701  -  Port does not
    exist<br/>-39737  -  Profile override setting is disabled.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        json_body (UpdateTheSwitchPortPoeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        port=port,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UpdateTheSwitchPortPoeEntity,
) -> Response[OperationResponseWithoutResult]:
    """Set poe mode for given port

     Set poe mode for given port. Please enable profile override first to use this
    interface.<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-39050  -  This device does not exist.<br/>-39701  -  Port does not
    exist<br/>-39737  -  Profile override setting is disabled.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        json_body (UpdateTheSwitchPortPoeEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        port=port,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UpdateTheSwitchPortPoeEntity,
) -> Optional[OperationResponseWithoutResult]:
    """Set poe mode for given port

     Set poe mode for given port. Please enable profile override first to use this
    interface.<br/><br/>The interface requires one of the permissions: <br/>DEVICES_WRITE<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-39050  -  This device does not exist.<br/>-39701  -  Port does not
    exist<br/>-39737  -  Profile override setting is disabled.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        json_body (UpdateTheSwitchPortPoeEntity):

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
            switch_mac=switch_mac,
            port=port,
            client=client,
            json_body=json_body,
        )
    ).parsed
