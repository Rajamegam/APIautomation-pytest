import pytest

from Utilities.configurations import config
from Utils.Assertions import AssertionUtils
from Utils.log_utils import logUtils


class TestDeleteInvoiceDetails:
    """Function to delete the invoice generated"""

    @pytest.mark.Regression
    @pytest.mark.order(5)
    # @pytest.mark.skip(reason=None)
    def test_delete_invoice_details(self, setup, shared_data):
        invoice_id = shared_data.get("invoice_id")
        try:
            response = setup.delete(
                endpoint=f"{config()['invoice endpoints']['invoice']}/{invoice_id}"
            )
        except Exception as e:
            logUtils.get_logger().critical(f"Cannot delete invoice{e}")
            pytest.fail("Cannot delete invoice")
        AssertionUtils.assert_status_code(response, 204)
