import json
from unittest.mock import MagicMock, patch

from src.carriers.handler import carrier_handler


@patch('src.carriers.fedex.api.requests.post', MagicMock())
def test_response_schema_success(expected_successfully_response):
    fedex = carrier_handler.carriers.get('FedEx')
    actual_response = json.loads(fedex.track('123124234234234').json())
    assert actual_response == expected_successfully_response
