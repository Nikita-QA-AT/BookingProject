import allure
import pytest
import requests


@allure.feature('Create booking')
@allure.story('Successful  booking creation')
def test_create_booking(api_client):

    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-22",
            "checkout": "2026-06-25"
        },
        "additionalneeds": "Breakfast"
    }


    response = api_client.create_booking(booking_data)


