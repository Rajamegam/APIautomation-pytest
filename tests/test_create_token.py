from Utils.api_helpers import APIHelper

api_helper = APIHelper()

payload_filepath = r"D:\API automation\Restful_Booker_Automation\data\create_token.json"


def test_create_token():
    response = api_helper.post('auth', payload_filepath)
    response_data = response.json()
    print(response_data.get("token", "Token not found"))
    return response
