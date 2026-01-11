from parking1 import (
    calculate_usage_score,
    determine_utilization_status,
    get_parking_utilization_summary
)


def test_calculate_usage_score():
    assert calculate_usage_score(10, 5) == 50
    assert calculate_usage_score(15, 6) == 90


def test_determine_utilization_status():
    assert determine_utilization_status(95) == "Over-Utilized Parking Area"
    assert determine_utilization_status(70) == "Optimally Utilized Parking Area"
    assert determine_utilization_status(40) == "Under-Utilized Parking Area"


def test_parking_utilization_summary():
    summary = get_parking_utilization_summary()

    assert summary["parking_area_name"] == "Main Campus Parking"
    assert summary["vehicle_type"] == "Car"
    assert summary["number_of_vehicles"] == 15
    assert summary["parking_hours"] == 6
    assert summary["usage_score"] == 90
    assert summary["utilization_status"] == "Over-Utilized Parking Area"