from unittest.mock import MagicMock, patch

from src.carriers.fedex.fedex import FedExAPI


@patch('src.carriers.fedex.fedex.requests.post')
def test_response_schema_success(response: MagicMock, response_data):
    response.return_value.status_code = 200
    response.return_value.text = response_data
    fedex = FedExAPI()
    fedex.track('123124234234234')
