from lab1.operations import *
from lab1.gcd import mod


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
    
    result1 = naive_modular_exponentiation(
        "12322",
        "1044",
        "1246576"
    )

    result2 = square_and_multiply(
            "256456",
            "589",
            "567879"
        )

    print("Result using naive base :", result1)
    print("Result using square and multiply : ", result2)