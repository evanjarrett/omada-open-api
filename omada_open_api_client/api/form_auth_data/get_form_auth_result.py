from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_form_auth_result_open_api_vo import OperationResponseFormAuthResultOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/surveys/auth-results/{surveyResultId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            surveyResultId=survey_result_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OperationResponseFormAuthResultOpenApiVO]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OperationResponseFormAuthResultOpenApiVO.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OperationResponseFormAuthResultOpenApiVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseFormAuthResultOpenApiVO]:
    """Get an authentication survey result for given surveyResultId

     Get an authentication survey's result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseFormAuthResultOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_result_id=survey_result_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseFormAuthResultOpenApiVO]:
    """Get an authentication survey result for given surveyResultId

     Get an authentication survey's result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseFormAuthResultOpenApiVO
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_result_id=survey_result_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseFormAuthResultOpenApiVO]:
    """Get an authentication survey result for given surveyResultId

     Get an authentication survey's result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseFormAuthResultOpenApiVO]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_result_id=survey_result_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseFormAuthResultOpenApiVO]:
    """Get an authentication survey result for given surveyResultId

     Get an authentication survey's result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>HOTSPOT_READ

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseFormAuthResultOpenApiVO
    """

    return (
        await asyncio_detailed(
            omadac_id=omadac_id,
            site_id=site_id,
            survey_result_id=survey_result_id,
            client=client,
        )
    ).parsed
