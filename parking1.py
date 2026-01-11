def calculate_usage_score(num_vehicles, hours):
    return num_vehicles * hours


def determine_utilization_status(usage_score):
    if usage_score >= 90:
        return "Over-Utilized Parking Area"
    elif 50 <= usage_score <= 89:
        return "Optimally Utilized Parking Area"
    else:
        return "Under-Utilized Parking Area"


def get_parking_utilization_summary():
    # Fixed values for Jenkins / CI
    parking_area_name = "Main Campus Parking"
    vehicle_type = "Car"
    number_of_vehicles = 15
    parking_hours = 6

    usage_score = calculate_usage_score(number_of_vehicles, parking_hours)
    utilization_status = determine_utilization_status(usage_score)

    return {
        "parking_area_name": parking_area_name,
        "vehicle_type": vehicle_type,
        "number_of_vehicles": number_of_vehicles,
        "parking_hours": parking_hours,
        "usage_score": usage_score,
        "utilization_status": utilization_status
    }


if __name__ == "__main__":
    summary = get_parking_utilization_summary()
    for key, value in summary.items():
        print(f"{key} : {value}")