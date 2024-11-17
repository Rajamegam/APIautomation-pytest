import pytest


class TestGetInvoiceDetails:
    @pytest.mark.Regression
    @pytest.mark.order(3)
    def test_get_invoice_details(self, setup, shared_data):
        invoice_id = shared_data.get("invoice_id")
        if not invoice_id:
            pytest.fail("Invoice ID not found in shared data")
        try:
            response = setup.get(endpoint=f"v2/invoicing/invoices/{invoice_id}")
        except Exception as e:
            setup.get_logger().error(f"Request to get invoice details failed: {e}")
            pytest.fail(f"Request to get invoice details failed: {e}")
        assert response is not None, "Expected response, but got None"
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        try:
            response_json = response.json()
            setup.get_logger().info(response_json)
        except ValueError as e:
            setup.get_logger().critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")
        response_invoice_id = response_json.get("id")
        assert response_invoice_id == invoice_id, (
            f"Invoice ID mismatch: expected {invoice_id}, but got {response_invoice_id}"
        )
        setup.get_logger().info(f"Successfully retrieved invoice details for ID: {invoice_id}")

