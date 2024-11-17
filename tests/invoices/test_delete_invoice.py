import pytest


class TestDeleteInvoiceDetails:
    @pytest.mark.Regression
    @pytest.mark.order(3)
    def test_delete_invoice_details(self, setup, shared_data):
        response = setup.delete(endpoint=f"v2/invoicing/invoices/{shared_data["invoice_id"]}")
        assert response.status_code == 204
