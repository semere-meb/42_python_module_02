#!/usr/bin/env python3


class Plant:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class PlantError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg


def water_one(plant: Plant) -> None:
    if plant.name is None:
        raise PlantError("invalid plant!")
    print(f"Watering {plant.name}")


def water_plants(plant_list: list) -> None:
    success: bool = False
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_one(plant)
        success = True
    except PlantError as e:
        print(f"Error: Cannot water {plant.name} - {e.msg}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_plant_checks():
    print("=== Garden watering system ===")

    plants: list = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots"),
    ]

    print("\nTesting normal watering...")
    water_plants(plants)

    print("\nTesting with error...")
    water_plants([Plant("tomato"), Plant(None)])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_plant_checks()
