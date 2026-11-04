
import random

from operations import compare, subtract
from modular import modular_power


def fermat_test(n, rounds=5):

    if not n.isdigit():
        raise ValueError("Enter a non-negative integer.")

    n = n.lstrip("0") or "0"

    if compare(n, "2") < 0:
        return False, 0

    if n == "2" or n == "3":
        return True, 0

    if n in ("4",):
        return False, 0

    # Random bases are selected from 2 to n-2.
    upper = subtract(n, "2")
    iterations = 0

    for i in range(rounds):

        # Convert to integer only for random base selection.
        a = str(random.randint(2, int(upper)))

        result, power_iterations = modular_power(
            a, subtract(n, "1"), n
        )

        iterations += 1

        if result != "1":
            return False, iterations

    return True, iterations


if __name__ == "__main__":

    numbers = ["7", "13", "15", "97", "100", "561"]

    for number in numbers:

        result, iterations = fermat_test(number)

        print("Number:", number)
        print("Probably prime:", result)
        print("Iterations:", iterations)
        print("----------------")
