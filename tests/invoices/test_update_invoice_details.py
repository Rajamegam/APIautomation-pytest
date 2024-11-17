import pytest

from Utilities.data_generator import update_invoice_details


class TestUpdateInvoiceDetails:
    @pytest.mark.Regression
    @pytest.mark.order(4)
    def test_update_invoice_details(self, setup, shared_data):
        invoice_id = shared_data.get("invoice_id")
        update_payload = update_invoice_details(invoice_id)
        try:
            response = setup.put(endpoint=f"v2/invoicing/invoices/{shared_data["invoice_id"]}",
                                 params={"send_to_recipient": "true", "send_to_invoicer": "true"},
                                 payload=update_payload)
        except Exception as e:
            setup.get_logger().critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        assert response.status_code == 200, setup.get_logger().critical(
            f"Expected status code 200 but received {response.status_code}")
        response_json = response.json()
        setup.get_logger().info(response_json)
