import pytest
from Utils.api_helpers import APIHelper

api_helper = APIHelper()
payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\create_token.json"


@pytest.fixture(scope='session', autouse=True)
def setup():
    response = api_helper.post('auth', payload_filepath)
    response_data = response.json()
    token = response_data.get("token")
    if token:
        api_helper.set_cookie_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper
