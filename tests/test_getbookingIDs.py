import pytest
from Utils.api_helpers import APIHelper

api_helper = APIHelper()


def test_get_bookingID_validation():
    response = api_helper.get('booking')
    print(response.json())
    assert response.status_code == 200
