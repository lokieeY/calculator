from crt import run_crt
from rsa import run_rsa, run_comparison


def main():
    while True:
        print("\n===== NUMBER THEORY =====")
        print("1. Solve CRT")
        print("2. RSA: key generation, encryption and decryption")
        print("3. Compare normal RSA and CRT-based RSA speed")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                run_crt()
            elif choice == "2":
                run_rsa()
            elif choice == "3":
                run_comparison()
            elif choice == "0":
                print("Exiting.")
                break
            else:
                print("Choose 0, 1, 2 or 3.")
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
