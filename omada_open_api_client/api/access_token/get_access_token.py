from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_token_response_v0 import AccessTokenResponseV0
from ...models.access_token_v0 import AccessTokenV0
from ...models.get_access_token_grant_type import GetAccessTokenGrantType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    json_body: AccessTokenV0,
    grant_type: GetAccessTokenGrantType,
    client_id: int,
    client_secret: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_grant_type = grant_type.value

    params["grant_type"] = json_grant_type

    params["client_id"] = client_id

    params["client_secret"] = client_secret

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "openapi/authorize/token",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AccessTokenResponseV0]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AccessTokenResponseV0.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AccessTokenResponseV0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AccessTokenV0,
    grant_type: GetAccessTokenGrantType,
    client_id: int,
    client_secret: str,
) -> Response[AccessTokenResponseV0]:
    """Get Access Token

     Get the access token for use with this API

    Args:
        grant_type (GetAccessTokenGrantType):
        client_id (int):
        client_secret (str):
        json_body (AccessTokenV0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessTokenResponseV0]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        grant_type=grant_type,
        client_id=client_id,
        client_secret=client_secret,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AccessTokenV0,
    grant_type: GetAccessTokenGrantType,
    client_id: int,
    client_secret: str,
) -> Optional[AccessTokenResponseV0]:
    """Get Access Token

     Get the access token for use with this API

    Args:
        grant_type (GetAccessTokenGrantType):
        client_id (int):
        client_secret (str):
        json_body (AccessTokenV0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessTokenResponseV0
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        grant_type=grant_type,
        client_id=client_id,
        client_secret=client_secret,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AccessTokenV0,
    grant_type: GetAccessTokenGrantType,
    client_id: int,
    client_secret: str,
) -> Response[AccessTokenResponseV0]:
    """Get Access Token

     Get the access token for use with this API

    Args:
        grant_type (GetAccessTokenGrantType):
        client_id (int):
        client_secret (str):
        json_body (AccessTokenV0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessTokenResponseV0]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        grant_type=grant_type,
        client_id=client_id,
        client_secret=client_secret,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AccessTokenV0,
    grant_type: GetAccessTokenGrantType,
    client_id: int,
    client_secret: str,
) -> Optional[AccessTokenResponseV0]:
    """Get Access Token

     Get the access token for use with this API

    Args:
        grant_type (GetAccessTokenGrantType):
        client_id (int):
        client_secret (str):
        json_body (AccessTokenV0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessTokenResponseV0
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
        )
    ).parsed
