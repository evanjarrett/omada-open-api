from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_response_without_result import OperationResponseWithoutResult
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    survey_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/openapi/v1/{omadacId}/sites/{siteId}/hotspot/surveys/{surveyId}".format(
            omadacId=omadac_id,
            siteId=site_id,
            surveyId=survey_id,
        ),
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
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Delete an existing authentication survey

     Delete an existing authentication survey by the given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_WRITE<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33004  -  Operation failed because other operations are being performed on this site. Please
    wait and try again later.<br/>-42054  -  The survey does not exist.<br/>-42057  -  The survey is in
    use, and you cannot edit or delete it.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The
    Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
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
) -> Optional[OperationResponseWithoutResult]:
    """Delete an existing authentication survey

     Delete an existing authentication survey by the given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_WRITE<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33004  -  Operation failed because other operations are being performed on this site. Please
    wait and try again later.<br/>-42054  -  The survey does not exist.<br/>-42057  -  The survey is in
    use, and you cannot edit or delete it.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The
    Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationResponseWithoutResult
    """

    return sync_detailed(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OperationResponseWithoutResult]:
    """Delete an existing authentication survey

     Delete an existing authentication survey by the given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_WRITE<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33004  -  Operation failed because other operations are being performed on this site. Please
    wait and try again later.<br/>-42054  -  The survey does not exist.<br/>-42057  -  The survey is in
    use, and you cannot edit or delete it.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The
    Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationResponseWithoutResult]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_id=survey_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    omadac_id: str,
    site_id: str,
    survey_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OperationResponseWithoutResult]:
    """Delete an existing authentication survey

     Delete an existing authentication survey by the given omadacId, siteId, surveyId.<br/><br/>The
    interface requires one of the permissions: <br/>HOTSPOT_WRITE<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33004  -  Operation failed because other operations are being performed on this site. Please
    wait and try again later.<br/>-42054  -  The survey does not exist.<br/>-42057  -  The survey is in
    use, and you cannot edit or delete it.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The
    Access Token has expired.

    Args:
        omadac_id (str):
        site_id (str):
        survey_id (str):

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
            survey_id=survey_id,
            client=client,
        )
    ).parsed
