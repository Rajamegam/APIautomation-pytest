class TestDeleteInvoiceDetails:
    def test_delete_invoice_details(self, setup, shared_data):
        response = setup.delete(endpoint=f"v2/invoicing/invoices/{shared_data["invoice_id"]}")
        assert response.status_code == 204
