import pytest

from Utilities.configurations import config
from Utilities.data_generator import update_invoice_details
from Utils.Assertions import AssertionUtils
from Utils.log_utils import get_logger


class TestUpdateInvoiceDetails:
    """ Function to update the invoice details
        Random invoice ID generated from the data generator
     """
    params = {"send_to_recipient": "true", "send_to_invoicer": "true"}

    @pytest.mark.Regression
    @pytest.mark.order(4)
    def test_update_invoice_details(self, setup, shared_data, logger):
        invoice_id = shared_data.get("invoice_id")
        update_payload = update_invoice_details(invoice_id)
        try:
            response = setup.put(endpoint=f"{config()['invoice endpoints']['invoice']}/{invoice_id}",
                                 params=self.params,
                                 payload=update_payload)
        except Exception as e:
            logger.critical(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")
        AssertionUtils.assert_presence_of_response(response)
        AssertionUtils.assert_status_code(response, 200)
        response_json = response.json()
        logger.info(response_json)
