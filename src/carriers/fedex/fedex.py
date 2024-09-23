from ..carrier import Carrier
from .adapter import ResponseBuilder
from .models import FedExCredentials

# only for presentation
FEDEX_USER_CREDENTIAL_KEY = 'mIAfOSJ0e32Zc4oV'
FEDEX_USER_CREDENTIAL_PASSWORD = 'gvTG2nBBVKwZq9dWJnBnJ7rVH'
FEDEX_PARENT_CREDENTIAL_KEY = 'HicUfijJZSUAtqAG'
FEDEX_PARENT_CREDENTIAL_PASSWORD = '2IX4AJyvWW9WltylOvw3RokcN'
FEDEX_ACCOUNT_NUMBER = '602091147'
FEDEX_METER_NUMBER = '118785166'


class FedEx(Carrier):
    name = 'FedEx'

    def __init__(self, api, api_url):
        self._api = api
        self._api_url = api_url

    def track(self, track_number: str):
        reply = self._api.track(track_number=track_number, credentials=self._get_credential(), api_url=self._api_url)
        return ResponseBuilder().build_track_response(self.name, track_number, reply)

    @staticmethod
    def _get_credential():
        return FedExCredentials(
            user_key=FEDEX_USER_CREDENTIAL_KEY,
            user_password=FEDEX_USER_CREDENTIAL_PASSWORD,
            parent_key=FEDEX_PARENT_CREDENTIAL_KEY,
            parent_password=FEDEX_PARENT_CREDENTIAL_PASSWORD,
            account_number=FEDEX_ACCOUNT_NUMBER,
            meter_number=FEDEX_METER_NUMBER,
        )
