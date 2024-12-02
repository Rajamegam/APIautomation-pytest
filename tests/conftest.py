import pytest
from Utils.BaseClass import BaseClass
from Utilities.configurations import *
from Utils.log_utils import get_logger

api_helper = BaseClass()


# Function level fixture to log in and share the access token to set_auth_token function in baseclass
@pytest.fixture(scope="function", autouse=False)
def setup(logger):
    logger, log_file = get_logger()
    payloads = {
        "grant_type": "client_credentials",
        "ignorecache": "true",
        "return_auth_schemas": "true",
        "return_client_metadata": "true",
        "return_unconsented_scopes": "true"
    }
    response = api_helper.post(endpoint=config()["invoice endpoints"]["login endpoint"], data=payloads,
                               auth=(
                                   config()['client details']['Client ID'],
                                   config()['client details']['Client Secret']))
    response_data = response.json()
    token = response_data.get("access_token")
    logger.info(token)
    if token:
        api_helper.set_auth_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper


""" This is a basic authorization """


@pytest.fixture(scope='session', autouse=False)
def basic_auth(logger):
    logger, log_file = get_logger()
    response = api_helper.post('auth', payload={
        "username": config()['credentials']['username'],
        "password": config()['credentials']['password']
    })
    response_data = response.json()
    token = response_data.get("token")
    logger.info(token)
    if token:
        api_helper.set_auth_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper


# shared data fixture to store and retrieve the commonly used variable across the functions
@pytest.fixture(scope="session")
def shared_data():
    data = {}
    return data


@pytest.fixture(scope="class")
def logger():
    # Initialize the logger once per test class
    logger, log_file = get_logger()
    return logger
