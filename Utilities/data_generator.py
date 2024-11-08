from faker import Faker

fake = Faker()


def create_booking_data():
    data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date_between(start_date="today", end_date="+10d").strftime("%Y-%m-%d"),
            "checkout": fake.date_between(start_date="+11d", end_date="+30d").strftime("%Y-%m-%d")
        },
        "additionalneeds": fake.word()
    }

    return data


def missing_required_fields():
    data = {
        "firstname": "king",
        "lastname": "Richard",
        "totalprice": None,
        "depositpaid": None,
        "bookingdates": {
            "checkin": "2024-10-01",
            "checkout": "2024-10-30"
        },
        "additionalneeds": "Breakfast"
    }
    return data
