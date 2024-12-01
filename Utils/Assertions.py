from Utils.BaseClass import BaseClass
from Utils.log_utils import logUtils

api_helper = BaseClass()


class AssertionUtils:

    # Function assert the status code of expected and actual outcome
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, (
            logUtils.get_logger().info(f"Expected status code {expected_code}, but got {response.status_code}")

        )

    # assert the presence of response
    @staticmethod
    def presence_of_response(response):
        assert response is not None, logUtils.get_logger().critical("Expected response, got None")
