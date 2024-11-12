import pytest
from Utilities.data_generator import create_draft_invoice  # Import function properly


@pytest.mark.dependency(depends=["test_generate_invoice_number"])
class TestCreateDraftInvoice:
    def test_create_draft_invoice(self, setup):
        draft_invoice_payload = create_draft_invoice()

        response = setup.post('v2/invoicing/invoices', payload=draft_invoice_payload)

        print(response.json())
