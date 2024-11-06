import pytest
from Utils.BaseClass import BaseClass
from Utilities.data_generator import create_booking_data

api_helper = BaseClass()


class TestCreateBooking():
    def test_create_booking(self):
        response = api_helper.post('booking', payload=create_booking_data())
        response_json = response.json()
        api_helper.get_logger().info(f"Response:{response_json}")
        bookingID = response_json.get('bookingid')
        if bookingID is None:
            api_helper.get_logger().warning("Booking ID not found in response")
        assert bookingID is not None, "Booking ID not found in response"
        api_helper.get_logger().info(f"Booking ID:{bookingID}")
        pytest.bookingID = bookingID
