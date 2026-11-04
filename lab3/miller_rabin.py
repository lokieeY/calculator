import random

from operations import compare, subtract,multiply,divide
from gcd import mod
from modular import modular_power


def miller_rabin(n, rounds=5):

    if not n.isdigit():
        raise ValueError("Enter a non-negative integer.")

    n = n.lstrip("0") or "0"

    if compare(n, "2") < 0:
        return False, 0

    if n == "2" or n == "3":
        return True, 0

    if mod(n, "2") == "0":
        return False, 0

    # Step 1: Write n-1 as 2^s * d
    d = subtract(n, "1")
    s = 0

    while mod(d, "2") == "0":
        d = divide(d, "2")
        s += 1

    iterations = 0

    # Step 2: Perform random rounds
    for _ in range(rounds):

        a = str(random.randint(2, int(subtract(n, "2"))))

        x, _ = modular_power(a, d, n)
        iterations += 1

        if x == "1" or x == subtract(n, "1"):
            continue

        passed = False

        # Step 3: Repeatedly square x
        for _ in range(s - 1):

            x = mod(multiply(x, x), n)

            if x == subtract(n, "1"):
                passed = True
                break

            if x == "1":
                return False, iterations

        if not passed:
            return False, iterations

    return True, iterations


if __name__ == "__main__":

    numbers = ["7", "13", "15", "97", "100", "561"]

    for number in numbers:

        result, iterations = miller_rabin(number)

        print("Number:", number)
        print("Probably prime:", result)
        print("Iterations:", iterations)
        print("----------------")