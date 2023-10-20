from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_list_form_auth_open_api_vo import OperationResponseListFormAuthOpenApiVO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_create_time: Union[Unset, None, str] = UNSET,
    sorts_answer_num: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sorts.name"] = sorts_name

    params["sorts.createTime"] = sorts_create_time

    params["sorts.answerNum"] = sorts_answer_num

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/surveys".format(
            omadacId=omadac_id,
            siteId=site_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseListFormAuthOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseListFormAuthOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseListFormAuthOpenApiVO]:
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
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_create_time: Union[Unset, None, str] = UNSET,
    sorts_answer_num: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseListFormAuthOpenApiVO]:
    """Get authentication survey list

     Get authentication survey list in a site by the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        sorts_name (Union[Unset, None, str]):
        sorts_create_time (Union[Unset, None, str]):
        sorts_answer_num (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListFormAuthOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        sorts_name=sorts_name,
        sorts_create_time=sorts_create_time,
        sorts_answer_num=sorts_answer_num,
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
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_create_time: Union[Unset, None, str] = UNSET,
    sorts_answer_num: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseListFormAuthOpenApiVO]:
    """Get authentication survey list

     Get authentication survey list in a site by the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        sorts_name (Union[Unset, None, str]):
        sorts_create_time (Union[Unset, None, str]):
        sorts_answer_num (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListFormAuthOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        client=client,
        sorts_name=sorts_name,
        sorts_create_time=sorts_create_time,
        sorts_answer_num=sorts_answer_num,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_create_time: Union[Unset, None, str] = UNSET,
    sorts_answer_num: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseListFormAuthOpenApiVO]:
    """Get authentication survey list

     Get authentication survey list in a site by the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        sorts_name (Union[Unset, None, str]):
        sorts_create_time (Union[Unset, None, str]):
        sorts_answer_num (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseListFormAuthOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        sorts_name=sorts_name,
        sorts_create_time=sorts_create_time,
        sorts_answer_num=sorts_answer_num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sorts_name: Union[Unset, None, str] = UNSET,
    sorts_create_time: Union[Unset, None, str] = UNSET,
    sorts_answer_num: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseListFormAuthOpenApiVO]:
    """Get authentication survey list

     Get authentication survey list in a site by the given omadacId, siteId.<br/><br/>The interface
    requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        sorts_name (Union[Unset, None, str]):
        sorts_create_time (Union[Unset, None, str]):
        sorts_answer_num (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseListFormAuthOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            client=client,
            sorts_name=sorts_name,
            sorts_create_time=sorts_create_time,
            sorts_answer_num=sorts_answer_num,
        )
    ).parsed
