from operations import *
from gcd import mod


def naive_modular_exponentiation(base, exponent, modulus):

    if modulus == "0":
        raise ValueError("Modulus cannot be zero")

    base = mod(base, modulus)

    result = "1"

    exponent = exponent.lstrip("0") or "0"

    while exponent != "0":

        result = multiply(result, base)
        result = mod(result, modulus)

        exponent = subtract(exponent, "1")

    return result



def square_and_multiply(base, exponent, modulus):
    
    if modulus == "0":
        raise ValueError("Modulus cannot be zero")

    base = mod(base, modulus)

    result = "1"

    exponent = exponent.lstrip("0") or "0"

    while exponent != "0":

        # Check whether exponent is odd
        remainder = mod(exponent, "2")

        if remainder == "1":

            result = multiply(result, base)
            result = mod(result, modulus)

        # Square the base
        base = multiply(base, base)
        base = mod(base, modulus)

        # Divide exponent by 2
        exponent = divide(exponent, "2")

    return result

if __name__ == "__main__":
    
    result = naive_modular_exponentiation(
        "2",
        "10",
        "1000"
    )

    print("Result:", result)