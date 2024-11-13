class TestGetInvoiceDetails:

    def test_get_invoice_details(self, setup):
        response = setup.get("v2/invoicing/invoices")
        print(response.json())
