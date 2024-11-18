from Utils.BaseClass import BaseClass

api_helper = BaseClass()


class AssertionUtils:

    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, (
            api_helper.get_logger().info(f"Expected status code {expected_code}, but got {response.status_code}")

        )
