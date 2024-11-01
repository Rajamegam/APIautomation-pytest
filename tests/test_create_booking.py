import pytest
from Utils.api_helpers import APIHelper

api_helper = APIHelper()

payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\create_booking.json"


def test_create_booking():
    response = api_helper.post('booking', payload_filepath)
    print(response.json())
    return response
