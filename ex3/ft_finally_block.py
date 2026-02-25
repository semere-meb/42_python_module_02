#!/usr/bin/env python3


class PlantError(Exception):
    pass


def water_one(name: str) -> None:
    if name is None:
        raise PlantError
    print(f"Watering {name}")


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_one(plant)
    except PlantError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden watering system ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None])

    print("\nCleanup always happens, even with errors!")
