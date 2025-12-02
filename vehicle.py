def vehicle_details(vehicle_number, owner_name, vehicle_type, year):
    result = (
        f"Vehicle Number:{vehicle_number} \n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of manufacture: {year}"
    )
    return result


if __name__ == "__main__":
    vehicle_number = "101"
    owner_name = "Rohit"
    vehicle_type = "Car"
    year = 2022
    print(vehicle_details(vehicle_number, owner_name, vehicle_type, year))
