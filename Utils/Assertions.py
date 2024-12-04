from Utils.BaseClass import BaseClass
from Utils.log_utils import get_logger

api_helper = BaseClass()


class AssertionUtils:

    # Function assert the status code of expected and actual outcome
    @staticmethod
    def assert_status_code(response, expected_code):
        logger, log_file = get_logger()
        assert response.status_code == expected_code, (
            logger.info(f"Expected status code {expected_code}, but got {response.status_code}")

        )

    # assert the presence of response body
    @staticmethod
    def assert_presence_of_response(response):
        logger, log_file = get_logger()
        assert response is not None, logger.critical("Expected response, got None")

    # Function assert the response time, if the actual response time is greater than the expected response time
    @staticmethod
    def assert_response_time(response, max_time):
        logger, log_file = get_logger()
        assert response.elapsed.total_seconds() > max_time(), logger.critical(
            f"Response time exceeded: {response.elapsed.total_seconds()}s"
        )

    # assert expected key and value is in the response
    @staticmethod
    def assert_response_contains(response, key, expected_value):
        logger, log_file = get_logger()
        assert key in response.json(), logger.critical(f"Key '{key}' not found in the response")
        assert response.json()[key] == expected_value, logger.critical(
            f"Expected value for '{key}' is {expected_value}, got {response.json()[key]}")



