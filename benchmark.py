import time

from exponentiation import (
    naive_modular_exponentiation,
    square_and_multiply
)


def measure_time(function, *args):

    start = time.perf_counter()

    result = function(*args)

    end = time.perf_counter()

    execution_time = end - start

    return result, execution_time


def run_benchmark():

    base = "2"
    modulus = "1000000007"

    exponents = [
        "10",
        "100",
        "500",
        "1000",
        "5000"
    ]

    print()
    print("Modular Exponentiation Benchmark")
    print("=" * 75)
    print(
        f"{'Exponent':<15}"
        f"{'Naive (s)':<20}"
        f"{'Square-Multiply (s)':<25}"
    )
    print("-" * 75)

    for exponent in exponents:
        naive_result, naive_time = measure_time(
            naive_modular_exponentiation,
            base,
            exponent,
            modulus
        )
        
        square_result, square_time = measure_time(
            square_and_multiply,
            base,
            exponent,
            modulus
        )

        # Verify both algorithms produce the same result
        if naive_result != square_result:
            print("ERROR: Results do not match!")
            return

        print(
            f"{exponent:<15}"
            f"{naive_time:<20.8f}"
            f"{square_time:<25.8f}"
        )


if __name__ == "__main__":
    run_benchmark()