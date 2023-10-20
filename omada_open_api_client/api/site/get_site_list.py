from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_grid_vo_site_summary_info import OperationResponseGridVOSiteSummaryInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    *,
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites".format(
            omadacId=omadac_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGridVOSiteSummaryInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGridVOSiteSummaryInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGridVOSiteSummaryInfo]:
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
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOSiteSummaryInfo]:
    """Get site list

     Get site list<br/><br/>The interface requires one of the permissions: <br/>GLOBAL_DASHBOARD_READ

    Args:
        omadac_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSiteSummaryInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOSiteSummaryInfo]:
    """Get site list

     Get site list<br/><br/>The interface requires one of the permissions: <br/>GLOBAL_DASHBOARD_READ

    Args:
        omadac_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSiteSummaryInfo
    """

    return sync_detailed(
        omadac_id=omadac_id,
        client=client,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        search_key=search_key,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOSiteSummaryInfo]:
    """Get site list

     Get site list<br/><br/>The interface requires one of the permissions: <br/>GLOBAL_DASHBOARD_READ

    Args:
        omadac_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOSiteSummaryInfo]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_name: Union[Unset, None, str] = UNSET,
    search_key: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOSiteSummaryInfo]:
    """Get site list

     Get site list<br/><br/>The interface requires one of the permissions: <br/>GLOBAL_DASHBOARD_READ

    Args:
        omadac_id (str):
        page (int):
        page_size (int):
        sorts_name (Union[Unset, None, str]):
        search_key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOSiteSummaryInfo
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            client=client,
            page=page,
            page_size=page_size,
            sorts_name=sorts_name,
            search_key=search_key,
        )
    ).parsed
