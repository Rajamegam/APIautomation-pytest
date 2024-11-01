import pytest
from Utils.api_helpers import APIHelper

api_helper = APIHelper()

payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\update_booking.json"
id = '506'


def test_update_booking(setup):
    api_helper = setup
    response = api_helper.put(f'booking/{id}', payload_filepath)
    if response is None:
        pytest.fail("PUT request failed, response is None")
    print(response.json())
    assert response.status_code == 200
