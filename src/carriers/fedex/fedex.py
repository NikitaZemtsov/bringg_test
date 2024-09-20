from pathlib import Path

import requests

from src.carriers.base_api import CarriersAPI
from src.carriers.fedex.models import FedExCredentialsModel
from src.carriers.fedex.schemas import ClientDetail, TrackReply, TrackRequest, WebAuthenticationDetail

FEDEX_API_URL = 'https://wsbeta.fedex.com:443/xml/track/v14'
FEDEX_USER_CREDENTIAL_KEY = 'mIAfOSJ0e32Zc4oV'
FEDEX_USER_CREDENTIAL_PASSWORD = 'gvTG2nBBVKwZq9dWJnBnJ7rVH'
FEDEX_PARENT_CREDENTIAL_KEY = 'HicUfijJZSUAtqAG'
FEDEX_PARENT_CREDENTIAL_PASSWORD = '2IX4AJyvWW9WltylOvw3RokcN'
FEDEX_ACCOUNT_NUMBER = '602091147'
FEDEX_METER_NUMBER = '118785166'


class FedExAPI(CarriersAPI):
    def get_credentional(self):
        return FedExCredentialsModel(
            user_key=FEDEX_USER_CREDENTIAL_KEY,
            user_password=FEDEX_USER_CREDENTIAL_PASSWORD,
            parent_key=FEDEX_PARENT_CREDENTIAL_KEY,
            parent_password=FEDEX_PARENT_CREDENTIAL_PASSWORD,
            account_number=FEDEX_ACCOUNT_NUMBER,
            meter_number=FEDEX_METER_NUMBER,
        )

    def track(self, track_number):
        credentials = self.get_credentional()
        web_authentication_detail = WebAuthenticationDetail.convert_to_xml_model(credentials)
        client_details = ClientDetail.convert_to_xml_model(credentials)
        track_request = TrackRequest(web_authentication_detail=web_authentication_detail, client_detail=client_details)
        track_request.selection_details.package_identifier.value = track_number
        return self.call_fedex_api(
            track_request.to_xml(xml_declaration=True, encoding='utf-8', skip_empty=True).decode('utf-8')
        )

    def call_fedex_api(self, xml_request):
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(FEDEX_API_URL, data=xml_request, headers=headers)

        if response.status_code == 200:  # noqa: PLR2004
            data = Path('fedex_mock.xml').read_text(encoding='UTF-8')
            return TrackReply.from_xml(data)
        return {'error': 'Failed to retrieve tracking details'}
