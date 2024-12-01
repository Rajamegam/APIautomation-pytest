import datetime

from Utilities.configurations import config


def product_json(row_data):
    return {
        "name": row_data.get("name", ""),
        "type": row_data.get("type", ""),
        "id": datetime.datetime.now(),
        "description": row_data.get("description", ""),
        "category": row_data.get("category", ""),
        "image_url": row_data.get("image url", ""),
        "home_url": row_data.get("homeurl", "")
    }


class TestCreateProduct:

    def test_create_product(self, setup):
        data = setup.read_data(file_path="D:/API automation/Restful_Booker_Automation/excel Data/ProductTestData.csv")
        row_data = data[0]
        payload = product_json(row_data=row_data)
        response = setup.post(endpoint=config()["product endpoints"]["create product"], payload=payload)
        print(response.json())
