import pytest

from Utilities.configurations import config
from Utils.Assertions import AssertionUtils
from Utils.BaseClass import BaseClass
from Utilities import *


class TestGenerateInvoiceNumber:
    """ This test function is used to generate invoice number.
    Once the invoice is generated, the invoice number is
    appended in the shared data fixture to access anywhere in the test
    """

    @pytest.mark.Regression
    @pytest.mark.order(1)
    def test_generate_invoice_number(self, setup, shared_data):
        try:
            response = setup.post(config()["invoice endpoints"]["generate invoice number"])
        except Exception as e:
            setup.get_logger().critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        AssertionUtils.presence_of_response(response)
        AssertionUtils.assert_status_code(response, 200)
        response_json = response.json()
        assert "invoice_number" in response_json, setup.get_logger().critical(
            "Response JSON does not contain 'invoice_number'"
        )
        invoice_number = response_json["invoice_number"]
        setup.get_logger().info(f"Generated invoice Number: {invoice_number}")
        print("invoice_number", invoice_number)
        shared_data["invoice_number"] = invoice_number

    def test_generate_invoice_number_unauthorized(self, setup):
        setup.header.pop("Authorization", None)
        response = setup.post("v2/invoicing/generate-next-invoice-number")
        AssertionUtils.assert_status_code(response, 401)
