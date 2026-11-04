import time

from trial_division import trial_division
from fermat_test import fermat_test
from miller_rabin import miller_rabin


def run_experiment():

    test_numbers = [
        "7",       # Small prime
        "97",      # Small prime
        "100",     # Composite
        "561",     # Carmichael number
        "1105",    # Carmichael number
        "1729",    # Carmichael number
        "104729",  # Prime
        "104730",  # Composite
        "1000003", # Prime
        "1000005"  # Composite
    ]

    algorithms = [
        ("Trial Division", trial_division),
        ("Fermat Test", fermat_test),
        ("Miller-Rabin", miller_rabin)
    ]

    for number in test_numbers:

        print("\nTesting number:", number)
        print("-" * 50)

        for name, algorithm in algorithms:

            start_time = time.perf_counter()

            result, iterations = algorithm(number)

            end_time = time.perf_counter()

            execution_time = end_time - start_time

            print("Algorithm:", name)
            print("Result:", result)
            print("Iterations:", iterations)
            print("Execution time:", execution_time)
            print("-" * 30)


if __name__ == "__main__":
    run_experiment()