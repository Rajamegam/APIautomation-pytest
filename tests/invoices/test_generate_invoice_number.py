import pytest

from Utils.BaseClass import BaseClass


class TestGenerateInvoiceNumber:
    @pytest.mark.order(1)
    def test_generate_invoice_number(self, setup, shared_data):
        try:
            response = setup.post("v2/invoicing/generate-next-invoice-number")
        except Exception as e:
            setup.get_logger().critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        assert response is not None, setup.get_logger().critical("Expected response, got None")
        assert response.status_code == 200, setup.get_logger().critical(
            f"Expected status code 200, got {response.status_code}"
        )
        response_json = response.json()
        assert "invoice_number" in response_json, setup.get_logger().critical(
            "Response JSON does not contain 'invoice_number'"
        )
        invoice_number = response_json["invoice_number"]
        setup.get_logger().info(f"Generated invoice Number: {invoice_number}")
        shared_data["invoice_number"] = invoice_number