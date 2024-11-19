from Utils.BaseClass import BaseClass

api_helper = BaseClass()


class AssertionUtils:

    # Function assert the status code of expected and actual outcome
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, (
            api_helper.get_logger().info(f"Expected status code {expected_code}, but got {response.status_code}")

        )

    # assert the presence of response
    @staticmethod
    def presence_of_response(response):
        assert response is not None, api_helper.get_logger().critical("Expected response, got None")
