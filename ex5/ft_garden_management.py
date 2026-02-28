#!/usr/bin/env python3


class GardenManager:
    def __init__(self, tank_level: int) -> None:
        self.tank_level = tank_level
        self.plants = []

    class GardenException(Exception):
        def __init__(self, msg: str) -> None:
            super().__init__(msg)

    class Plant:
        def __init__(
            self,
            name: str,
            water_level: int,
            water_cost: int,
            sunlight_hours: int,
        ) -> None:
            if name == "":
                raise GardenManager.GardenException(
                    "Error adding plant: Plant name cannot be empty!"
                )
            self.name = name
            self.water_level = water_level
            self.water_consumption = water_cost
            self.sunlight_hours = sunlight_hours
            print(f"Added {name} successfylly")

        def water_plant(self, tank_level: int) -> int:
            if tank_level < self.water_consumption:
                raise GardenManager.GardenException(
                    f"Not enough water in tank for {self.name}"
                )
            print(f"Watering {self.name} - success")
            return tank_level - self.water_consumption

        def check_health(self) -> None:
            if not 1 <= self.water_level <= 10:
                raise GardenManager.GardenException(
                    f"Error checking {self.name}: "
                    + f"Water level {self.water_level} is too "
                    + f"{'high' if self.water_level > 10 else 'low'} (1 - 10)"
                )
            if not 2 <= self.sunlight_hours <= 12:
                raise GardenManager.GardenException(
                    f"Error checking {self.name}: "
                    + f"Sunlight hours {self.sunlight_hours} is too "
                    + f"{'high' if self.sunlight_hours > 12 else 'low'}"
                    + "(2 - 12)"
                )
            print(
                f"{self.name}: healthy (water: {self.water_level}, "
                + f"sun: {self.sunlight_hours})"
            )

    def add_plant(
        self, name: str, water_level: int, water_cost: int, sunlight_hours: int
    ) -> None:
        self.plants[:0] = [
            self.Plant(name, water_level, water_cost, sunlight_hours),
        ]

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            self.tank_level = plant.water_plant(self.tank_level)

    def check_plant_health(self) -> None:
        for plant in self.plants:
            plant.check_health()

    def check_tank_level(self) -> None:
        if self.tank_level < 10:
            raise self.GardenException("GardenError: Not enough water in tank")


def test_garden_management() -> None:
    plants = [
        ("Lettuce", 15, 20, 8),
        ("Tomato", 5, 30, 8),
        ("", 5, 15, 8),
    ]
    garden_mgr = GardenManager(50)

    print("\nAdding plants to garden...")
    try:
        for plant in plants:
            garden_mgr.add_plant(*plant)
    except GardenManager.GardenException as e:
        print(e)

    print("\nWatering plants..")
    try:
        garden_mgr.water_plants()
    except GardenManager.GardenException as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden_mgr.check_plant_health()
    except GardenManager.GardenException as e:
        print(e)
    # finally:
    #     print("Stopping health checks")

    print("\nTesting error recovery...")
    try:
        garden_mgr.check_tank_level()
    except GardenManager.GardenException:
        print("Caught GardenError: Not enough water in tank")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
