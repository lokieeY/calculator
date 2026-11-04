from operations import *
from gcd import mod
from extended_gcd import extended_gcd


def modular_addition(a, b, m):
    
    #Calculate (a + b) mod m

    if m == "0":
        raise ValueError("Modulus cannot be zero")

    result = add(a, b)
    return mod(result, m)


def modular_multiplication(a, b, m):
    
    #Calculate (a * b) mod m
    
    if m == "0":
        raise ValueError("Modulus cannot be zero")

    result = multiply(a, b)
    return mod(result, m)


def modular_inverse(a, m):
    
    #a^(-1) mod m exists only when gcd(a, m) = 1.
    if m == "0":
        raise ValueError("Modulus cannot be zero")

    g, x, y = extended_gcd(a, m)

    if g != "1":
        raise ValueError(
            "Modular inverse does not exist"
        )

    # x is a SignedNumber
    if x.negative:
        x_value = mod(x.value, m)

        if x_value == "0":
            return "0"

        return subtract(m, x_value)

    return mod(x.value, m)


def modular_power(base, exponent, modulus):
    """
    Calculate (base ^ exponent) mod modulus
    using repeated squaring.
    """

    if modulus == "0":
        raise ValueError("Modulus cannot be zero.")

    if not base.isdigit() or not exponent.isdigit() or not modulus.isdigit():
        raise ValueError("Enter non-negative integers.")

    result = mod("1", modulus)
    base = mod(base, modulus)

    iterations = 0

    while exponent != "0":

        iterations += 1

        # Check whether exponent is odd.
        if mod(exponent, "2") == "1":
            result = mod(multiply(result, base), modulus)

        # Square the base.
        base = mod(multiply(base, base), modulus)

        # Divide exponent by 2.
        exponent = divide(exponent, "2")

    return result, iterations


if __name__ == "__main__":
    
    print("Modular Addition:")
    print(modular_addition("20034566743242", "15354678554", "745678"))

    print("\nModular Multiplication:")
    print(modular_multiplication("1345670", "15346575", "468742"))

    print("\nModular Inverse:")
    print(modular_inverse("3", "11"))

    print("\nModular power:")
    result, iterations = modular_power("2", "10", "17")
    print("Result:", result)
    print("Iterations:", iterations)