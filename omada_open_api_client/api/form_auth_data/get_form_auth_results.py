from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_grid_vo_form_auth_result_open_api_vo import (
    OperationResponseGridVOFormAuthResultOpenApiVO,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    page: int,
    page_size: int,
    sorts_form_auth: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.formAuth"] = sorts_form_auth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/surveys/{surveyId}/auth-results".format(
            omadacId=omadac_id,
            siteId=site_id,
            surveyId=survey_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseGridVOFormAuthResultOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseGridVOFormAuthResultOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseGridVOFormAuthResultOpenApiVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_form_auth: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOFormAuthResultOpenApiVO]:
    """Get authentication result lists for given survey

     Get an authentication survey's result list with given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):
        page (int):
        page_size (int):
        sorts_form_auth (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOFormAuthResultOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
        page=page,
        page_size=page_size,
        sorts_form_auth=sorts_form_auth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_form_auth: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOFormAuthResultOpenApiVO]:
    """Get authentication result lists for given survey

     Get an authentication survey's result list with given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):
        page (int):
        page_size (int):
        sorts_form_auth (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOFormAuthResultOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
        client=client,
        page=page,
        page_size=page_size,
        sorts_form_auth=sorts_form_auth,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_form_auth: Union[Unset, None, str] = UNSET,
) -> Response[OperationResponseGridVOFormAuthResultOpenApiVO]:
    """Get authentication result lists for given survey

     Get an authentication survey's result list with given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):
        page (int):
        page_size (int):
        sorts_form_auth (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseGridVOFormAuthResultOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
        page=page,
        page_size=page_size,
        sorts_form_auth=sorts_form_auth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: int,
    page_size: int,
    sorts_form_auth: Union[Unset, None, str] = UNSET,
) -> Optional[OperationResponseGridVOFormAuthResultOpenApiVO]:
    """Get authentication result lists for given survey

     Get an authentication survey's result list with given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):
        page (int):
        page_size (int):
        sorts_form_auth (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseGridVOFormAuthResultOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            survey_id=survey_id,
            client=client,
            page=page,
            page_size=page_size,
            sorts_form_auth=sorts_form_auth,
        )
    ).parsed
