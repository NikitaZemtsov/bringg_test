from pathlib import Path

import pytest


@pytest.fixture()
def response_data():
    return Path('fedex_mock.xml').read_text(encoding='UTF-8')
