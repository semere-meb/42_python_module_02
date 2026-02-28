#!/usr/bin/env python3


def garden_operations(name: str, t_str: str, t_max: int, f_name: str) -> int:
    plants: dict = {"apple": "Vitamin A"}

    try:
        temp: int = int(t_str)
        temp_status: int = temp / t_max
        open(f_name, "r")
        nutrition: str = plants[name]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{f_name}'")
    except KeyError:
        print(f"Caught KeyError: {name}")
    except (TypeError, IndexError):
        print("Caught an error, but program continues!")
    else:
        print(
            f"{name}: temp ({temp}), temp % ({temp_status * 100}%), "
            + f"nutrition: {nutrition}"
        )


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("apple", "ab", 100, "missing.txt")

    print("\nTesting ZeroDivisionError...")
    garden_operations("apple", "40", 0, "missing.txt")

    print("\nTesting FileNotFoundError")
    garden_operations("apple", "40", 100, "missing.txt")

    print("\nTesting KeyError...")
    garden_operations("orange", "23", 10, "ex1/ft_different_errors.py")

    print("\nTesting multiple errors together...")
    garden_operations("orange", "23", "100", "missing.txt")

    print("\nTesting an OK case...")
    garden_operations("apple", "18", 30, "ex1/ft_different_errors.py")


if __name__ == "__main__":
    test_error_types()
