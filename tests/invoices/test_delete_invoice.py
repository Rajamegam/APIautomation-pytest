import pytest

from Utilities.configurations import config
from Utils.Assertions import AssertionUtils


class TestDeleteInvoiceDetails:
    """Function to delete the invoice generated"""

    @pytest.mark.Regression
    @pytest.mark.order(5)
    # @pytest.mark.skip(reason=None)
    def test_delete_invoice_details(self, setup, shared_data,logger):
        invoice_id = shared_data.get("invoice_id")
        try:
            response = setup.delete(
                endpoint=f"{config()['invoice endpoints']['invoice']}/{invoice_id}"
            )
        except Exception as e:
            logger.critical(f"Cannot delete invoice{e}")
            pytest.fail("Cannot delete invoice")
        AssertionUtils.assert_status_code(response, 204)
