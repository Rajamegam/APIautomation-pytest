import pytest


@pytest.mark.dependency(depends=["test_create_draft_invoice"])
class TestGetInvoiceDetails:
    def test_get_invoice_details(self, setup, shared_data):
        invoice_id = shared_data.get("invoice_id")

        if not invoice_id:
            pytest.fail("Invoice ID not found in shared data")

        response = setup.get(endpoint=f"v2/invoicing/invoices/{invoice_id}")

        assert response.status_code == 200, "Failed to retrieve invoice details"
        assert response.json().get("id") == invoice_id, "Invoice ID mismatch in response"

        print(response.json())
