from datetime import datetime

import pytest
import requests
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
    api_helper.get_logger().info(token)
    if token:
        api_helper.set_cookie_token(token)
    else:
        pytest.fail("Authentication failed; token not retrieved")

    yield api_helper


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     reports_dir = "D://API automation//Restful_Booker_Automation//reports"
#     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     config.option.htmlpath = f"{reports_dir}/report_{now}.html"
