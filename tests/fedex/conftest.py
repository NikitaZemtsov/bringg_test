import json
from pathlib import Path

import pytest


@pytest.fixture()
def expected_successfully_response():
    file_path = Path(__file__).parent / 'successfully_response.json'
    with file_path.open() as file:
        return json.load(file)
