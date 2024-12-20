import pytest

from Utilities.configurations import config
from Utils.Assertions import AssertionUtils
from Utils.log_utils import get_logger


class TestGetInvoiceDetails:
    """ Function to get all the invoice details by passing the invoice ID.
        Invoice ID is retrieved from the shared data fixture
    """
    get_all_invoice_params = {"page": "1", "page_size": "10", "total_required": "true", "fields": "amount"}
    id_list = []

    @pytest.mark.Regression
    @pytest.mark.order(3)
    # Get the details of the one particular invoice by sending the invoice ID
    def test_get_invoice_details(self, setup, shared_data, logger):
        invoice_id = shared_data.get("invoice_id")
        if not invoice_id:
            pytest.fail("Invoice ID not found in shared data")
        try:
            response = setup.get(
                endpoint=f"{config()['invoice endpoints']['invoice']}/{invoice_id}"
            )
        except Exception as e:
            logger.error(f"Request to get invoice details failed: {e}")
            pytest.fail(f"Request to get invoice details failed: {e}")
        assert response is not None, "Expected response, but got None"
        AssertionUtils.assert_status_code(response, 200)
        # assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        try:
            response_json = response.json()
            logger.info(response_json)
        except ValueError as e:
            logger.critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")
        response_invoice_id = response_json.get("id")
        assert response_invoice_id == invoice_id, (
            f"Invoice ID mismatch: expected {invoice_id}, but got {response_invoice_id}"
        )
        logger.info(f"Successfully retrieved invoice details for ID: {invoice_id}")

    # Get all the invoice details and check whether invoice ID and invoice number is present in the list
    def test_get_all_invoice_details(self, setup, shared_data, logger):
        try:
            response = setup.get(endpoint=config()['invoice endpoints']['invoice'], params=self.get_all_invoice_params)
        except Exception as e:
            logger.critical(f"Request to get the invoice list{e}")
            pytest.fail("Request to get the invoice list")
        response_details = response.json()
        AssertionUtils.assert_status_code(response, 200)
        self.id_list = [data["id"] for data in response_details["items"]]
        logger.info(f"List of invoice ID: {self.id_list}")
        logger.info(f"{shared_data.get("invoice_id")} is present in the list" if shared_data.get(
            "invoice_id") in self.id_list else "ID not present")
