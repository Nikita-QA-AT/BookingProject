import allure
import pytest
from pydantic import ValidationError
from requests import HTTPError
from core.models.booking import BookingResponse


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
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
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")


    assert "bookingid" in response
    assert isinstance(response["bookingid"], int)
    assert response['booking']["firstname"] == booking_data["firstname"]
    assert response['booking']["lastname"] == booking_data["lastname"]
    assert response['booking']["totalprice"] == booking_data["totalprice"]
    assert response['booking']["depositpaid"] == booking_data["depositpaid"]
    assert response['booking']["bookingdates"]['checkin'] == booking_data["bookingdates"]['checkin']
    assert response['booking']["bookingdates"]['checkout'] == booking_data["bookingdates"]['checkout']
    assert response['booking']["additionalneeds"] == booking_data["additionalneeds"]


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert "bookingid" in response
    assert isinstance(response["bookingid"], int)
    assert response['booking']["firstname"] == generate_random_booking_data["firstname"]
    assert response['booking']["lastname"] == generate_random_booking_data["lastname"]
    assert response['booking']["totalprice"] == generate_random_booking_data["totalprice"]
    assert response['booking']["depositpaid"] == generate_random_booking_data["depositpaid"]
    assert response['booking']["bookingdates"]['checkin'] == generate_random_booking_data["bookingdates"]['checkin']
    assert response['booking']["bookingdates"]['checkout'] == generate_random_booking_data["bookingdates"]['checkout']
    assert response['booking']["additionalneeds"] == generate_random_booking_data["additionalneeds"]


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with empty body')
def test_create_booking_with_empty_body(api_client):
    with pytest.raises(HTTPError):
        api_client.create_booking({})


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking without firstname')
def test_create_booking_without_firstname(api_client):
    booking_data = {
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-22",
            "checkout": "2026-06-25"
        },
        "additionalneeds": "Breakfast"
    }

    with pytest.raises(HTTPError):
        api_client.create_booking(booking_data)
