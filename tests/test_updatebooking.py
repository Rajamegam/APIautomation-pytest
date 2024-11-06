import pytest
from Utils.api_helpers import APIHelper
from Utilities.data_generator import create_booking_data

api_helper = APIHelper()


class TestUpdateBooking:
    @pytest.mark.dependency(depends=["test_create_booking"])
    def test_update_booking(self, setup):
        api_helper = setup
        bookingID = getattr(pytest, 'bookingID', None)
        # assert bookingID is not None, "Booking ID should not be None. Ensure test_create_booking sets it."

        response = api_helper.put(f'booking/{bookingID}', payload=create_booking_data())
        if response is None:
            pytest.fail("PUT request failed, response is None")

        print(response.json())
        assert response.status_code == 200
