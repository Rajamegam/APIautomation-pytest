import pytest
from Utilities.data_generator import create_draft_invoice


class TestCreateDraftInvoice:
    @pytest.mark.dependency(depends=["TestGenerateInvoiceNumber::test_generate_invoice_number"])
    def test_create_draft_invoice(self, setup, shared_data):
        invoice_number = shared_data.get("invoice_number")
        draft_invoice_payload = create_draft_invoice(invoice_number)
        response = setup.post('v2/invoicing/invoices', payload=draft_invoice_payload)
        response_json = response.json()
        invoice_id = response_json.get("id")
        shared_data["invoice_id"] = invoice_id
        print(response.json())
