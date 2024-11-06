import pytest
from Utils.BaseClass import BaseClass
from Utilities.data_generator import create_booking_data

api_helper = BaseClass()


class TestCreateBooking():
    @pytest.mark.dependency()
    def test_create_booking(self):
        response = api_helper.post('booking', payload=create_booking_data())
        response_json = response.json()
        api_helper.get_logger().info(response_json)
        print(response_json)
        bookingID = response_json.get('bookingid')
        assert bookingID is not None, "Booking ID not found in response"
        print(f"Booking ID is {bookingID}")
        pytest.bookingID = bookingID
        return bookingID
