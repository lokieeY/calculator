from time import perf_counter

from operations import add, subtract, multiply, divide, compare
from gcd import mod, gcd
from modular import modular_inverse


def modular_power(base, exponent, modulus):
    # Calculate (base ** exponent) mod modulus by repeated squaring.
    if modulus == "0":
        raise ValueError("Modulus must not be zero.")

    result = "1"
    base = mod(base, modulus)

    while exponent != "0":
        if mod(exponent, "2") == "1":
            result = mod(multiply(result, base), modulus)

        base = mod(multiply(base, base), modulus)
        exponent = divide(exponent, "2")

    return result


def generate_keys(p, q, e):
    # This assignment version expects the user to enter prime p and q.
    if p == q or p == "0" or q == "0":
        raise ValueError("p and q must be different positive primes.")

    n = multiply(p, q)
    phi = multiply(subtract(p, "1"), subtract(q, "1"))

    if compare(e, "1") <= 0 or compare(e, phi) >= 0:
        raise ValueError("Choose e such that 1 < e < phi(n).")

    if gcd(e, phi) != "1":
        raise ValueError("e and phi(n) must be coprime.")

    d = modular_inverse(e, phi)
    return n, phi, d


def encrypt(message, e, n):
    if compare(message, n) >= 0:
        raise ValueError("Message must be smaller than n.")
    return modular_power(message, e, n)


def decrypt_normal(ciphertext, d, n):
    return modular_power(ciphertext, d, n)


def decrypt_crt(ciphertext, p, q, d):
    # Decrypt separately modulo p and q.
    dp = mod(d, subtract(p, "1"))
    dq = mod(d, subtract(q, "1"))

    m1 = modular_power(ciphertext, dp, p)
    m2 = modular_power(ciphertext, dq, q)

    # Combine m1 and m2 using the inverse of q modulo p.
    q_inverse = modular_inverse(q, p)

    if compare(m1, m2) >= 0:
        difference = subtract(m1, m2)
    else:
        difference = subtract(add(m1, p), m2)

    h = mod(multiply(q_inverse, difference), p)
    message = add(m2, multiply(h, q))

    # Return the message and values useful for explaining CRT.
    details = {
        "dp": dp,
        "dq": dq,
        "m1": m1,
        "m2": m2,
        "q_inverse_mod_p": q_inverse,
        "h": h
    }
    return message, details


def run_rsa():
    print("\nRSA")
    p = input("Enter prime p: ").strip()
    q = input("Enter prime q: ").strip()
    e = input("Enter public exponent e: ").strip()

    n, phi, d = generate_keys(p, q, e)
    print("Public key (e, n):", "(" + e + ", " + n + ")")
    print("Private exponent d:", d)
    print("n =", n, "phi(n) =", phi)

    print("\n1. Encrypt a message, then decrypt it")
    print("2. Compare normal and CRT decryption")
    choice = input("Choose: ").strip()

    if choice == "1":
        message = input("Enter message number (smaller than n): ").strip()
        ciphertext = encrypt(message, e, n)
        print("Ciphertext:", ciphertext)
    elif choice == "2":
        ciphertext = input("Enter ciphertext (smaller than n): ").strip()
    else:
        print("Invalid choice.")
        return

    if not ciphertext.isdigit() or compare(ciphertext, n) >= 0:
        print("Ciphertext must be a non-negative number smaller than n.")
        return

    normal = decrypt_normal(ciphertext, d, n)
    crt_result, details = decrypt_crt(ciphertext, p, q, d)

    print("Normal RSA decryption:", normal)
    print("CRT-based RSA decryption:", crt_result)
    print("Both results match:", normal == crt_result)
    print("CRT intermediate values:")
    for name, value in details.items():
        print(name + " =", value)


def compare_decryption_times(p, q, e, ciphertext, repetitions=3):
    # Time both methods using the same key and ciphertext.
    n, phi, d = generate_keys(p, q, e)

    start = perf_counter()
    for _ in range(repetitions):
        normal = decrypt_normal(ciphertext, d, n)
    normal_time = (perf_counter() - start) / repetitions

    start = perf_counter()
    for _ in range(repetitions):
        crt_result, details = decrypt_crt(ciphertext, p, q, d)
    crt_time = (perf_counter() - start) / repetitions

    return normal, crt_result, normal_time, crt_time


def run_comparison():
    print("\nCompare normal RSA and CRT-based RSA")
    p = input("Enter prime p: ").strip()
    q = input("Enter prime q: ").strip()
    e = input("Enter public exponent e: ").strip()

    n, phi, d = generate_keys(p, q, e)
    ciphertext = input("Enter ciphertext (smaller than n): ").strip()

    if not ciphertext.isdigit() or compare(ciphertext, n) >= 0:
        print("Ciphertext must be a non-negative number smaller than n.")
        return

    normal, crt_result, normal_time, crt_time = compare_decryption_times(
        p, q, e, ciphertext
    )

    print("Normal RSA result:", normal)
    print("CRT-based RSA result:", crt_result)
    print("Results match:", normal == crt_result)
    print("Average normal decryption time:", normal_time, "seconds")
    print("Average CRT decryption time:", crt_time, "seconds")
    print("Note: small examples and custom string arithmetic can make timing noisy.")
