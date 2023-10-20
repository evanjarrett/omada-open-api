from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_site_entity import CreateSiteEntity
from ...models.operation_response_object import OperationResponseObject
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    json_body: CreateSiteEntity,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/sites".format(
            omadacId=omadac_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseObject]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseObject.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateSiteEntity,
) -> Response[OperationResponseObject]:
    """Create new site

     Create new site<br/><br/>The interface requires one of the permissions:
    <br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-33101  -  This name already
    exists. Please enter another name for this site.<br/>-33104  -  The number of sites has reached the
    limit.

    Args:
        omadac_id (str):
        json_body (CreateSiteEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateSiteEntity,
) -> Optional[OperationResponseObject]:
    """Create new site

     Create new site<br/><br/>The interface requires one of the permissions:
    <br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-33101  -  This name already
    exists. Please enter another name for this site.<br/>-33104  -  The number of sites has reached the
    limit.

    Args:
        omadac_id (str):
        json_body (CreateSiteEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return sync_detailed(
        omadac_id=omadac_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateSiteEntity,
) -> Response[OperationResponseObject]:
    """Create new site

     Create new site<br/><br/>The interface requires one of the permissions:
    <br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-33101  -  This name already
    exists. Please enter another name for this site.<br/>-33104  -  The number of sites has reached the
    limit.

    Args:
        omadac_id (str):
        json_body (CreateSiteEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseObject]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateSiteEntity,
) -> Optional[OperationResponseObject]:
    """Create new site

     Create new site<br/><br/>The interface requires one of the permissions:
    <br/>GLOBAL_DASHBOARD_WRITE<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-33101  -  This name already
    exists. Please enter another name for this site.<br/>-33104  -  The number of sites has reached the
    limit.

    Args:
        omadac_id (str):
        json_body (CreateSiteEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseObject
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
