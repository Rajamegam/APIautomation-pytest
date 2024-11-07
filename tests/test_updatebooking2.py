from Utils.BaseClass import BaseClass
from Utilities.data_generator import create_booking_data

api_helper = BaseClass()


class TestUpdateBooking:
    def test_update_booking(self, setup):
        api_helper = setup

        response = api_helper.put(f'booking/7738', payload=create_booking_data())
        response_json = response.json()
        print(response_json)