from datetime import datetime

import pytest
import requests
from Utils.BaseClass import BaseClass
from Utilities.configurations import *

api_helper = BaseClass()


@pytest.fixture(scope='module', autouse=True)
def setup():
    payloads = {
        "grant_type": "client_credentials",
        "ignorecache": "true",
        "return_auth_schemas": "true",
        "return_client_metadata": "true",
        "return_unconsented_scopes": "true"
    }
    response = api_helper.post("v1/oauth2/token", data=payloads,
                               auth=(
                                   config()['client details']['Client ID'],
                                   config()['client details']['Client Secret']))
    response_data = response.json()
    token = response_data.get("access_token")
    api_helper.get_logger().info(token)
    if token:
        api_helper.set_auth_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper

    # @pytest.hookimpl(tryfirst=True)
    # def pytest_configure(config):
    #     reports_dir = "D://API automation//Restful_Booker_Automation//reports"
    #     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     config.option.htmlpath = f"{reports_dir}/report_{now}.html"
