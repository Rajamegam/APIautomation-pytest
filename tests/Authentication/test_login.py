from Utilities.configurations import config
from Utils.Assertions import AssertionUtils


class TestLogin:
    """ Functions that checks for valid and invalid authentication"""
    payloads = {
        "grant_type": "client_credentials",
        "ignorecache": "true",
        "return_auth_schemas": "true",
        "return_client_metadata": "true",
        "return_unconsented_scopes": "true"
    }

    def test_valid_login(self, setup):
        response = setup.post(endpoint=config()["invoice endpoints"]["login endpoint"], data=self.payloads,
                              auth=(
                                  config()['client details']['Client ID'],
                                  config()['client details']['Client Secret']))
        response_data = response.json()
        # token = response_data.get("access_token")
        AssertionUtils.assert_status_code(response, 200)

    def test_invalid_login(self, setup):
        response = setup.post(endpoint=config()["invoice endpoints"]["login endpoint"], data=self.payloads,
                              auth=(
                                  config()['client details'],
                                  config()['client details']))
        response_data = response.json()
        token = response_data.get("access_token")
        AssertionUtils.assert_status_code(response, 401)
