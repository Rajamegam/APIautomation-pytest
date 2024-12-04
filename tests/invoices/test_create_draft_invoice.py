import pytest

from Utilities.configurations import config
from Utilities.data_generator import create_draft_invoice
from Utils.Assertions import AssertionUtils


class TestCreateDraftInvoice:
    """ Creates the draft invoice
        get the invoice number from the shared data fixture
        insert the generated invoice ID in the shared data fixture for access for other tests
    """

    @pytest.mark.Regression
    @pytest.mark.order(2)
    def test_create_draft_invoice(self, setup, shared_data, logger):
        invoice_number = shared_data.get("invoice_number")
        draft_invoice_payload = create_draft_invoice(invoice_number)
        try:
            response = setup.post(config()["invoice endpoints"]["invoice"], payload=draft_invoice_payload)
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        AssertionUtils.assert_presence_of_response(response)
        AssertionUtils.assert_status_code(response, 201)
        try:
            response_json = response.json()
        except ValueError as e:
            logger.critical(f"Failed to parse JSON response: {e}")
            pytest.fail(f"Failed to parse JSON response: {e}")
        invoice_id = response_json.get("id")
        assert invoice_id, "Invoice ID is missing in the response JSON"
        logger.info(f"Generated Invoice ID is: {invoice_id}")
        shared_data["invoice_id"] = invoice_id
