import allure



@allure.feature('Create booking')
@allure.story('Successful  booking creation')
def test_create_booking(api_client, generate_random_booking_data):

    response = api_client.create_booking(generate_random_booking_data)

    assert "bookingid" in response

    booking = response["booking"]

    assert booking["firstname"] == generate_random_booking_data["firstname"]
    assert booking["lastname"] == generate_random_booking_data["lastname"]
    assert booking["totalprice"] == generate_random_booking_data["totalprice"]
    assert booking["depositpaid"] == generate_random_booking_data["depositpaid"]
    assert booking["additionalneeds"] == generate_random_booking_data["additionalneeds"]
    assert booking["bookingdates"] == generate_random_booking_data["bookingdates"]


