import pytest

from Utils.BaseClass import BaseClass

api_helper = BaseClass()


def test_generate_invoice_number(setup, shared_data):
    response = setup.post("v2/invoicing/generate-next-invoice-number")
    assert response is not None, "Expected response, got None"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_json = response.json()
    assert "invoice_number" in response_json, "Response JSON does not contain 'invoice_number'"
    invoice_number = response_json.get("invoice_number")
    shared_data[invoice_number] = invoice_number
    print(invoice_number)
    return invoice_number
