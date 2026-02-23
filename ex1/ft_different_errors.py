def garden_operations(name: str, t_str: str, t_max: int, f_name: str) -> int:
    plants = {"apple": "Vitamin A"}

    try:
        temp = int(t_str)
        temp_status = temp / t_max
        open(f_name, "r")
        nutrition = plants[name]
    except ValueError:
        print(f"Error: '{t_str}' is not a valid temperature value")
    except ZeroDivisionError:
        print(f"Invalid maximum temperature {t_max}")
    except FileNotFoundError:
        print(f"File {f_name} not found")
    except KeyError:
        print(f"{name} not found in your garden")
    except (TypeError, ValueError):
        print("Caught an error, but program continues!")
    else:
        print(
            f"{name}: temp ({temp}), temp % ({temp_status * 100}%), "
            + f"nutrition: {nutrition}"
        )


def test_error_types() -> None:
    open("temp.txt", "w")
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("apple", "ab", 100, "temp.txt")

    print("\nTesting ZeroDivisionError...")
    garden_operations("apple", "40", 0, "temp.txt")

    print("\nTesting FileNotFoundError")
    garden_operations("apple", "40", 100, "ddata.txt")

    print("\nTesting KeyError...")
    garden_operations("orange", "40", 100, "temp.txt")

    print("\nTesting multiple errors together...")
    garden_operations("orange", "40", "100", "temp.txt")

    print("\nTesting an OK case...")
    garden_operations("apple", "40", 100, "temp.txt")


if __name__ == "__main__":
    test_error_types()
