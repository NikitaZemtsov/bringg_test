from pathlib import Path

from ..carrier_api import CarrierAPI
from .models import FedExCredentialsModel
from .schemas import ClientDetail, TrackReply, TrackRequest, WebAuthenticationDetail


class FedExAPI(CarrierAPI):
    def track(self, track_number: str, credentials: FedExCredentialsModel, api_url: str):
        web_authentication_detail = WebAuthenticationDetail.convert_to_xml_model(credentials)
        client_details = ClientDetail.convert_to_xml_model(credentials)
        track_request = TrackRequest(web_authentication_detail=web_authentication_detail, client_detail=client_details)
        track_request.selection_details.package_identifier.value = track_number
        return self.call_fedex_api(
            track_request.to_xml(xml_declaration=True, encoding='utf-8', skip_empty=True).decode('utf-8'), api_url
        )

    @staticmethod
    def call_fedex_api(xml_request, api_url):  # noqa: ARG004
        # headers = {'Content-Type': 'application/xml'} noqa: ERA001
        # response = requests.post(api_url, data=xml_request, headers=headers) noqa: ERA001
        # FedEx test server is not working well. There is only 1 response for every 10 requests.
        # if response.status_code == 200:
        data = (Path(__file__).parent / 'fedex_mock.xml').read_text(encoding='UTF-8')
        return TrackReply.from_xml(data)
