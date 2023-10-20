from omada_open_api_client import AuthenticatedClient, Client
from omada_open_api_client.api.access_token import get_access_token
from omada_open_api_client.api.client import get_client_list
from omada_open_api_client.models import ClientInfo, AccessTokenV0, GetAccessTokenGrantType, AccessTokenResponseV0

access_token = ""
BASE_URL="https://omada.com"
OMADA_ID="111111"
SITE_ID="222222"
CLIENT_ID="3333333"
CLIENT_SECRET="444444"

tokenclient = Client(base_url=BASE_URL, verify_ssl=False)


with tokenclient as tokenclient:
    response: AccessTokenResponseV0 = get_access_token.sync(client=tokenclient, 
                                     grant_type=GetAccessTokenGrantType.CLIENT_CREDENTIALS,
                                     client_id=CLIENT_ID,
                                     client_secret=CLIENT_SECRET,
                                     json_body=AccessTokenV0.from_dict({"omadacId": OMADA_ID})
                                     )
    print(response)
    access_token = response.result.access_token

authclient = AuthenticatedClient(
    base_url=BASE_URL, prefix="AccessToken=", token=access_token, verify_ssl=False
)

with authclient as authclient:
    ci_list: [ClientInfo] = get_client_list.sync(
        client=authclient,
        omadac_id=OMADA_ID,
        site_id=SITE_ID,
        page=1,
        page_size=100,
    )
    print(ci_list)
