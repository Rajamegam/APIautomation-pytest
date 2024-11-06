import pytest
from Utils.BaseClass import BaseClass
from Utilities.configurations import *

api_helper = BaseClass()


@pytest.fixture(scope='session', autouse=True)
def setup():
    response = api_helper.post('auth', payload={
        "username": config()['credentials']['username'],
        "password": config()['credentials']['password']
    })
    response_data = response.json()
    token = response_data.get("token")
    if token:
        api_helper.set_cookie_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper
