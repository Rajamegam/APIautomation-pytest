import pytest
from Utils.BaseClass import BaseClass
from Utilities.data_generator import *

api_helper = BaseClass()


class TestCreateBooking:

    # TC001 - Create a Booking with valid Data
    @pytest.mark.smoke
    def test_create_booking(self, setup):
        response = api_helper.post('booking', payload=create_booking_data())
        response_json = response.json()
        api_helper.get_logger().info(f"Response:{response_json}")
        bookingID = response_json.get('bookingid')
        if bookingID is None:
            api_helper.get_logger().warning("Booking ID not found in response")
        assert bookingID is not None, "Booking ID not found in response"
        api_helper.get_logger().info(f"Booking ID:{bookingID}")
        pytest.bookingID = bookingID

    # TC002 - Create booking with missing fields
    def test_create_booking_with_missing_fields(self, setup):
        response = api_helper.post('booking', payload=missing_required_fields())
        assert response is None








