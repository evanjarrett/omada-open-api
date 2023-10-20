from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_port_setting_config_entity import GatewayPortSettingConfigEntity
from ...models.operation_response_gateway_port_setting_config_entity import (
    OperationResponseGatewayPortSettingConfigEntity,
)
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    port: str,
    *,
    json_body: GatewayPortSettingConfigEntity,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/gateways/{gatewayMac}/ports/{port}/config".format(
            omadacId=omadac_id,
            siteId=site_id,
            gatewayMac=gateway_mac,
            port=port,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGatewayPortSettingConfigEntity]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGatewayPortSettingConfigEntity.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGatewayPortSettingConfigEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GatewayPortSettingConfigEntity,
) -> Response[OperationResponseGatewayPortSettingConfigEntity]:
    """Modify gateway port config

     Modify gateway port config<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-39501  -  This gateway does not
    exist.<br/>-39507  -  Gateway mirroring port reaches max limit.<br/>-39706  -  Please choose at
    least one port or LAG to be mirrored.<br/>-39718  -  Mirrored ports contain invalid port.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        port (str):
        json_body (GatewayPortSettingConfigEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGatewayPortSettingConfigEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
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
    gateway_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GatewayPortSettingConfigEntity,
) -> Optional[OperationResponseGatewayPortSettingConfigEntity]:
    """Modify gateway port config

     Modify gateway port config<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-39501  -  This gateway does not
    exist.<br/>-39507  -  Gateway mirroring port reaches max limit.<br/>-39706  -  Please choose at
    least one port or LAG to be mirrored.<br/>-39718  -  Mirrored ports contain invalid port.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        port (str):
        json_body (GatewayPortSettingConfigEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGatewayPortSettingConfigEntity
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        port=port,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GatewayPortSettingConfigEntity,
) -> Response[OperationResponseGatewayPortSettingConfigEntity]:
    """Modify gateway port config

     Modify gateway port config<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-39501  -  This gateway does not
    exist.<br/>-39507  -  Gateway mirroring port reaches max limit.<br/>-39706  -  Please choose at
    least one port or LAG to be mirrored.<br/>-39718  -  Mirrored ports contain invalid port.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        port (str):
        json_body (GatewayPortSettingConfigEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGatewayPortSettingConfigEntity]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        port=port,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    port: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GatewayPortSettingConfigEntity,
) -> Optional[OperationResponseGatewayPortSettingConfigEntity]:
    """Modify gateway port config

     Modify gateway port config<br/><br/>The interface requires one of the permissions:
    <br/>DEVICES_WRITE<br/><br/>The possible error code for the interface in the returned body is one of
    the following error codes (non generic error codes): <br/>-39501  -  This gateway does not
    exist.<br/>-39507  -  Gateway mirroring port reaches max limit.<br/>-39706  -  Please choose at
    least one port or LAG to be mirrored.<br/>-39718  -  Mirrored ports contain invalid port.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        port (str):
        json_body (GatewayPortSettingConfigEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGatewayPortSettingConfigEntity
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            gateway_mac=gateway_mac,
            port=port,
            client=client,
            json_body=json_body,
        )
    ).parsed
