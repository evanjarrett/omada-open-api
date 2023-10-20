from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_list_string import OperationResponseListString
from ...models.scenario import Scenario
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    json_body: Scenario,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/openapi/v1/{omadacId}/scenarios".format(
            omadacId=omadac_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseListString]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseListString.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseListString]:
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
    json_body: Scenario,
) -> Response[OperationResponseListString]:
    """Create new scenario

     Create new scenario<br/><br/>The interface requires one of the permissions: <br/>NETWORK_WRITE

    Args:
        omadac_id (str):
        json_body (Scenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListString]
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
    json_body: Scenario,
) -> Optional[OperationResponseListString]:
    """Create new scenario

     Create new scenario<br/><br/>The interface requires one of the permissions: <br/>NETWORK_WRITE

    Args:
        omadac_id (str):
        json_body (Scenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListString
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
    json_body: Scenario,
) -> Response[OperationResponseListString]:
    """Create new scenario

     Create new scenario<br/><br/>The interface requires one of the permissions: <br/>NETWORK_WRITE

    Args:
        omadac_id (str):
        json_body (Scenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListString]
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
    json_body: Scenario,
) -> Optional[OperationResponseListString]:
    """Create new scenario

     Create new scenario<br/><br/>The interface requires one of the permissions: <br/>NETWORK_WRITE

    Args:
        omadac_id (str):
        json_body (Scenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListString
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
