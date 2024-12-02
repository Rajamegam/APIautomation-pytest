import os

import pytest
from Utilities.configurations import config
from Utils.Assertions import AssertionUtils
from Utils.log_utils import logUtils


def product_json(row_data):
    return {
        "name": row_data.get("name", ""),
        "type": row_data.get("type", ""),
        "id": row_data.get("id", ""),
        "description": row_data.get("description", ""),
        "category": row_data.get("category", ""),
        "image_url": row_data.get("imageurl", ""),
        "home_url": row_data.get("homeurl", "")
    }


class TestCreateProduct:
    """
    This class is used for testing Product creation. Test methods read data from a CSV file,
    append values to the 'product_json' function, and send them as JSON payloads.
    """

    test_records_path = os.path.join("excel Data", "productstestrecords.csv")

    def test_create_product(self, setup):  # TC1: Positive test case with valid data
        logger = logUtils.get_logger()
        try:
            data = setup.read_data(file_path=self.test_records_path)
            row_data = data[0]
            payload = product_json(row_data=row_data)
        except Exception as e:
            logger.critical(f"Cannot load data from the CSV: {e}")
            pytest.fail(f"Cannot load data from the CSV: {e}")

        try:
            response = setup.post(
                endpoint=config()["product endpoints"]["create product"],
                payload=payload
            )
            AssertionUtils.presence_of_response(response)
            AssertionUtils.assert_status_code(response, 201)
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")

        try:
            response_json = response.json()
            logger.info(f"Response JSON: {response_json}")
        except ValueError as e:
            logger.critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")

    def test_create_product_empty_name(self, setup):  # TC2: whether getting 400 status for empty 'name' value
        logger = logUtils.get_logger()
        try:
            data = setup.read_data(file_path=self.test_records_path)
            row_data = data[1]
            payload = product_json(row_data=row_data)
        except Exception as e:
            logger.critical(f"Cannot load data from the CSV: {e}")
            pytest.fail(f"Cannot load data from the CSV: {e}")

        try:
            response = setup.post(
                endpoint=config()["product endpoints"]["create product"],
                payload=payload
            )
            AssertionUtils.presence_of_response(response)
            AssertionUtils.assert_status_code(response, 400)
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")

        try:
            response_json = response.json()
            logger.info(f"Response JSON: {response_json}")
        except ValueError as e:
            logger.critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")

    def test_create_product_invalid_data_type(self, setup):
        # TC3: whether getting 400 status for invalid datatype for 'type' value
        logger = logUtils.get_logger()
        try:
            data = setup.read_data(file_path=self.test_records_path)
            row_data = data[2]
            payload = product_json(row_data=row_data)
        except Exception as e:
            logger.critical(f"Cannot load data from the CSV: {e}")
            pytest.fail(f"Cannot load data from the CSV: {e}")

        try:
            response = setup.post(
                endpoint=config()["product endpoints"]["create product"],
                payload=payload
            )
            AssertionUtils.presence_of_response(response)
            AssertionUtils.assert_status_code(response, 400)
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")

        try:
            response_json = response.json()
            logger.info(f"Response JSON: {response_json}")
        except ValueError as e:
            logger.critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")
