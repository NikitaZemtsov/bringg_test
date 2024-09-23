from pathlib import Path

import requests

from ..carrier_api import CarrierAPI
from .models import FedExCredentials
from .schemas import ClientDetail, TrackReply, TrackRequest, WebAuthenticationDetail


class FedExAPI(CarrierAPI):
    def track(self, track_number: str, credentials: FedExCredentials, api_url: str) -> TrackReply:
        web_authentication_detail = WebAuthenticationDetail.convert_to_xml_model(credentials)
        client_details = ClientDetail.convert_to_xml_model(credentials)
        track_request = TrackRequest(web_authentication_detail=web_authentication_detail, client_detail=client_details)
        track_request.selection_details.package_identifier.value = track_number
        response = self._call_fedex_api(  # noqa:  F841
            track_request.to_xml(xml_declaration=True, encoding='utf-8', skip_empty=True).decode('utf-8'), api_url
        )
        # mock response due to FedEx test server is not working well. There is only 1 response for every 10 requests.
        data = (Path(__file__).parent / 'fedex_mock.xml').read_text(encoding='UTF-8')
        return TrackReply.from_xml(data)

    @staticmethod
    def _call_fedex_api(xml_request, api_url):
        headers = {'Content-Type': 'application/xml'}
        return requests.post(api_url, data=xml_request, headers=headers)
