import pytest
from Utils.api_helpers import APIHelper

api_helper = APIHelper()

payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\create_booking.json"


@pytest.mark.dependency()
def test_create_booking():
    response = api_helper.post('booking', payload_filepath)
    response_json = response.json()
    bookingID = response_json['bookingid']
    print(f"Booking ID is ", bookingID)
    return bookingID
