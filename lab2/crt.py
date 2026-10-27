from operations import add, subtract, multiply, divide, compare
from gcd import mod, gcd
from modular import modular_inverse


def solve_crt(residues, moduli):
    # Start with the first congruence.
    x = mod(residues[0], moduli[0])
    current_modulus = moduli[0]

    # Add each remaining congruence.
    for i in range(1, len(residues)):
        a = mod(residues[i], moduli[i])
        n = moduli[i]
        g = gcd(current_modulus, n)

        # Calculate (a - x) mod n without using negative numbers.
        x_mod_n = mod(x, n)
        if compare(a, x_mod_n) >= 0:
            difference = subtract(a, x_mod_n)
        else:
            difference = subtract(add(a, n), x_mod_n)

        # A solution exists only if gcd divides the difference.
        if mod(difference, g) != "0":
            raise ValueError("These congruences have no common solution.")

        left = divide(current_modulus, g)
        right = divide(n, g)

        # Find the multiplier k.
        if right == "1":
            k = "0"
        else:
            difference = divide(difference, g)
            inverse = modular_inverse(mod(left, right), right)
            k = mod(multiply(difference, inverse), right)

        # Update the answer and its modulus.
        x = add(x, multiply(current_modulus, k))
        current_modulus = multiply(current_modulus, right)
        x = mod(x, current_modulus)

    return x, current_modulus


def run_crt():
    print("\nCRT: solve x = a (mod n)")
    try:
        count = int(input("How many congruences? "))
        if count < 1:
            print("Enter at least one congruence.")
            return

        residues = []
        moduli = []

        for i in range(count):
            print("Congruence", i + 1)
            a = input("Enter a: ").strip()
            n = input("Enter positive n: ").strip()

            if not a.isdigit() or not n.isdigit() or n == "0":
                print("Enter non-negative a and positive n using digits.")
                return

            residues.append(a)
            moduli.append(n)

        answer, combined_modulus = solve_crt(residues, moduli)
        print("Solution: x =", answer, "(mod", combined_modulus, ")")
        print("Smallest non-negative solution:", answer)

    except ValueError as error:
        print("Error:", error)
