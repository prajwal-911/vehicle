from vehicle import vehicle_details

def test_vehicle_details():
    expected_output = (
        "Vehicle Number:101 \n"
        "Owner Name: Rohit\n"
        "Vehicle Type: Car\n"
        "Year of manufacture: 2020"
    )

    assert vehicle_details("101", "Rohit", "Car", "2020") == expected_output
