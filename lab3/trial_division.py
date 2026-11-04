
from operations import add, multiply, compare
from gcd import mod


def trial_division(n):

    if not n.isdigit():
        raise ValueError("Enter a non-negative integer.")

    n = n.lstrip("0") or "0"

    # Numbers smaller than 2 are not prime.
    if compare(n, "2") < 0:
        return False, 0

    # Start checking from divisor 2.
    divisor = "2"
    iterations = 0

    while compare(multiply(divisor, divisor), n) <= 0:

        iterations += 1

        # Check whether divisor divides n.
        if mod(n, divisor) == "0":
            return False, iterations

        # Move to the next divisor.
        divisor = add(divisor, "1")

    return True, iterations


if __name__ == "__main__":

    numbers = ["7", "13", "15", "97", "100"]

    for number in numbers:

        result, iterations = trial_division(number)

        print("Number:", number)
        print("Prime:", result)
        print("Iterations:", iterations)
        print("----------------")
