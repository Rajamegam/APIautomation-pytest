import pytest

from Utilities.configurations import config


class TestDeleteInvoiceDetails:
    @pytest.mark.Regression
    @pytest.mark.order(5)
    #@pytest.mark.skip(reason=None)
    def test_delete_invoice_details(self, setup, shared_data):
        invoice_id = shared_data.get("invoice_id")
        try:
            response = setup.delete(
                endpoint=f"{config()['invoice endpoints']['invoice']}/{invoice_id}"
            )
        except Exception as e:
            setup.get_logger().critical(f"Cannot delete invoice{e}")
            pytest.fail("Cannot delete invoice")
        assert response.status_code == 204
