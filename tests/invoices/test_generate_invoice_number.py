import pytest

from Utilities.configurations import config
from Utils.Assertions import AssertionUtils



class TestGenerateInvoiceNumber:
    """ This test function is used to generate invoice number.
    Once the invoice is generated, the invoice number is
    appended in the shared data fixture to access anywhere in the test method
    """

    @pytest.mark.Regression
    @pytest.mark.order(1)
    def test_generate_invoice_number(self, setup, shared_data,logger):
        try:
            response = setup.post(config()["invoice endpoints"]["generate invoice number"])
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        AssertionUtils.assert_presence_of_response(response)
        AssertionUtils.assert_status_code(response, 200)
        response_json = response.json()
        assert "invoice_number" in response_json, logger.critical(
            "Response JSON does not contain 'invoice_number'"
        )
        invoice_number = response_json["invoice_number"]
        logger.info(f"Generated invoice Number: {invoice_number}")
        shared_data["invoice_number"] = invoice_number

    def test_generate_invoice_number_unauthorized(self, setup):
        setup.header.pop("Authorization", None)
        response = setup.post("v2/invoicing/generate-next-invoice-number")
        AssertionUtils.assert_status_code(response, 401)
