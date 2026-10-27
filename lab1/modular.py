from lab1.operations import *
from lab1.gcd import mod
from lab1.extended_gcd import extended_gcd


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

if __name__ == "__main__":
    
    print("Modular Addition:")
    print(modular_addition("20034566743242", "15354678554", "745678"))

    print("\nModular Multiplication:")
    print(modular_multiplication("1345670", "15346575", "468742"))

    print("\nModular Inverse:")
    print(modular_inverse("3", "11"))