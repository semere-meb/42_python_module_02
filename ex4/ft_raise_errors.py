#!/usr/bin/env python3


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int)\
        -> str:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty")
    if not 1 <= water_level <= 10:
        raise ValueError(
            f"Water level {water_level} is too "
            + f"{'high' if water_level > 10 else 'low'} (1 - 10)"
        )
    if not 2 <= sunlight_hours <= 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too "
            + f"{'high' if sunlight_hours > 12 else 'low'} (2 - 12)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    plants = [
        ("Testing  good values...", ("tomato", 7, 7)),
        ("Testing empty plant name...", ("", 7, 7)),
        ("Testing bad water level...", ("tomato", 15, 7)),
        ("Testing bad sunlight hours...", ("tomato", 7, 0)),
    ]

    print("=== Garden Plant Health Checker ===")
    for plant in plants:
        print("\n" + plant[0])
        try:
            res = check_plant_health(*plant[1])
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(res)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
