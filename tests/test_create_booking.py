import pytest
from Utils.api_helpers import APIHelper
from Utilities.data_generator import create_booking_data

api_helper = APIHelper()


# @pytest.mark.dependency()
# def test_create_booking():
#     response = api_helper.post('booking', payload=create_booking_data())
#     response_json = response.json()
#     bookingID = response_json['bookingid']
#     print(f"Booking ID is ", bookingID)
#     pytest.bookingID = bookingID


@pytest.mark.dependency()
def test_create_booking():
    response = api_helper.post('booking', payload=create_booking_data())
    response_json = response.json()
    print(response_json)
    bookingID = response_json.get('bookingid')
    assert bookingID is not None, "Booking ID not found in response"
    print(f"Booking ID is {bookingID}")
    pytest.bookingID = bookingID
