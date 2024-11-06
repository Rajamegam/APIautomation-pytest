import pytest
from Utils.BaseClass import BaseClass

api_helper = BaseClass()


class TestGetBookingDetails:
    def test_get_bookingID_validation(self):
        response = api_helper.get('booking')
        print(response.json())
        assert response.status_code == 200
