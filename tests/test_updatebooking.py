import pytest
from Utils.api_helpers import APIHelper
from tests.test_create_booking import test_create_booking

api_helper = APIHelper()

payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\update_booking.json"


@pytest.mark.dependency(depends=["test_create_booking"])
def test_update_booking(setup, bookingID):
    api_helper = setup
    response = api_helper.put(f'booking/{bookingID}', payload_filepath)
    if response is None:
        pytest.fail("PUT request failed, response is None")
    print(response.json())
    assert response.status_code == 200
