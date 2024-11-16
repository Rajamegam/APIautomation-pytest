import pytest
from Utilities.data_generator import create_draft_invoice


class TestCreateDraftInvoice:
    @pytest.mark.order(2)
    def test_create_draft_invoice(self, setup, shared_data):
        invoice_number = shared_data.get("invoice_number")
        draft_invoice_payload = create_draft_invoice(invoice_number)
        try:
            response = setup.post('v2/invoicing/invoices', payload=draft_invoice_payload)
        except Exception as e:
            setup.get_logger().critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        assert response is not None, "Expected response, but got None"
        assert response.status_code == 201, f"Expected 200, but got {response.status_code}"
        try:
            response_json = response.json()
        except ValueError as e:
            setup.get_logger().critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")
        invoice_id = response_json.get("id")
        assert invoice_id, "Invoice ID is missing in the response JSON"
        setup.get_logger().info(f"Generated Invoice ID is: {invoice_id}")
        shared_data["invoice_id"] = invoice_id

