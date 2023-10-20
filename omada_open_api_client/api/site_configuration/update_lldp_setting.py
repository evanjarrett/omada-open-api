from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_without_result import OperationResponseWithoutResult
from ...models.site_settinglldp import SiteSettinglldp
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    json_body: SiteSettinglldp,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/lldp".format(
            omadacId=omadac_id,
            siteId=site_id,
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
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SiteSettinglldp,
) -> Response[OperationResponseWithoutResult]:
    """Modify site lldp setting

     Modify site lldp setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_WRITE<br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1300  -
    Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (SiteSettinglldp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
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
    json_body: SiteSettinglldp,
) -> Optional[OperationResponseWithoutResult]:
    """Modify site lldp setting

     Modify site lldp setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_WRITE<br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1300  -
    Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (SiteSettinglldp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
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
    json_body: SiteSettinglldp,
) -> Response[OperationResponseWithoutResult]:
    """Modify site lldp setting

     Modify site lldp setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_WRITE<br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1300  -
    Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (SiteSettinglldp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
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
    json_body: SiteSettinglldp,
) -> Optional[OperationResponseWithoutResult]:
    """Modify site lldp setting

     Modify site lldp setting<br/><br/>The interface requires one of the permissions:
    <br/>NETWORK_WRITE<br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1300  -
    Failed to get site information.

    Args:
        omadac_id (str):
        site_id (str):
        json_body (SiteSettinglldp):

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
            client=client,
            json_body=json_body,
        )
    ).parsed
