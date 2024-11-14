import pytest
from Utilities.data_generator import create_draft_invoice
from tests.invoices.test_generate_invoice_number import shared_data


class TestCreateDraftInvoice:
    # @pytest.mark.dependency(depends=["TestGenerateInvoiceNumber::test_generate_invoice_number"], scope="session")
    @pytest.mark.order(2)
    def test_create_draft_invoice(self, setup):
        # Logic for test_create_draft_invoice that depends on test_generate_invoice_number
        invoice_number = shared_data.get("invoice_number")
        draft_invoice_payload = create_draft_invoice(invoice_number)
        response = setup.post('v2/invoicing/invoices', payload=draft_invoice_payload)
        response_json = response.json()
        invoice_id = response_json.get("id")
        print(invoice_id)
        shared_data["invoice_id"] = invoice_id
        print(shared_data)
        print(response.json())
