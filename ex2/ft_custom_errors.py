class Plant:
    def __init__(self, name: str, water_level: int, status: str) -> None:
        self.name = name
        self.water_level = water_level
        self.status = status


class GardenError(Exception):
    def __init__(self, plants: list(Plant)) -> None:
        self.plants = plants
        self.msg = "Garden can't be empty"


class PlantError(GardenError):
    def __init__(self, plant: Plant) -> None:
        super().__init__([plant])
        self.msg = f"The {self.plants[0].name} plant is wilting!"


class WaterError(GardenError):
    def __init__(self, plant: Plant) -> None:
        super().__init__([plant])
        self.msg = f"Not enough water in the tank({self.plants[0].water_lev})!"


def check_garden(plants: list(Plant)):
    if plants == []:
        raise GardenError(plants)


def check_plant_status(plant: Plant) -> object:
    if plant.status == "wilting":
        raise PlantError(plant)


def check_plant_water_level(plant: Plant) -> object:
    if plant.water_level < 15:
        raise WaterError(plant)


def demo_func() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    p1 = Plant("Tomato", 20, "wilting")
    try:
        check_plant_status(p1)
    except PlantError as e:
        print("Caught PlantError " + e.msg)

    print("\nTesting WaterError")
    p2 = Plant("Tomato", 10, "Growing")
    try:
        check_plant_water_level(p2)
    except WaterError as e:
        print("Caught WaterError " + e.msg)

    print("\nTesting catching all garden errors...")
    for plant in p1, p2:
        try:
            check_plant_status(plant)
            check_plant_water_level(plant)
        except GardenError as e:
            print("Caught a garden error: " + e.msg)
    try:
        check_garden([])
    except GardenError as e:
        print("Caught a garden error: " + e.msg)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    demo_func()
