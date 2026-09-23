import customtkinter as ctk

from gcd import gcd
from extended_gcd import extended_gcd, signed_to_string


app = ctk.CTk()

app.title("GCD Calculator")
app.geometry("500x500")


# --------------------------------
# Calculate GCD
# --------------------------------

def calculate_gcd():

    try:
        # Keep input as strings
        a = first_number.get()
        b = second_number.get()

        # Check empty input
        if a == "" or b == "":
            result_label.configure(
                text="Please enter both numbers"
            )
            return

        result = gcd(a, b)

        result_label.configure(
            text=f"GCD = {result}"
        )

    except ValueError:
        result_label.configure(
            text="Please enter valid numbers"
        )


# --------------------------------
# Calculate Extended GCD
# --------------------------------

def calculate_extended_gcd():

    try:
        # Keep input as strings
        a = first_number.get()
        b = second_number.get()

        # Check empty input
        if a == "" or b == "":
            result_label.configure(
                text="Please enter both numbers"
            )
            return

        result, x, y = extended_gcd(a, b)

        # Convert SignedNumber objects to strings
        x = signed_to_string(x)
        y = signed_to_string(y)

        result_label.configure(
            text=f"GCD = {result}\nx = {x}\ny = {y}"
        )

    except ValueError:
        result_label.configure(
            text="Please enter valid numbers"
        )


# --------------------------------
# First Number
# --------------------------------

label_first = ctk.CTkLabel(
    app,
    text="First Number"
)

label_first.pack(pady=10)


first_number = ctk.CTkEntry(
    app,
    width=350,
    height=40
)

first_number.pack(pady=10)


# --------------------------------
# Second Number
# --------------------------------

label_second = ctk.CTkLabel(
    app,
    text="Second Number"
)

label_second.pack(pady=10)


second_number = ctk.CTkEntry(
    app,
    width=350,
    height=40
)

second_number.pack(pady=10)


# --------------------------------
# GCD Button
# --------------------------------

gcd_button = ctk.CTkButton(
    app,
    text="Calculate GCD",
    command=calculate_gcd
)

gcd_button.pack(pady=20)


# --------------------------------
# Extended GCD Button
# --------------------------------

extended_gcd_button = ctk.CTkButton(
    app,
    text="Calculate Extended GCD",
    command=calculate_extended_gcd
)

extended_gcd_button.pack(pady=10)


# --------------------------------
# Result
# --------------------------------

result_label = ctk.CTkLabel(
    app,
    text="Result = "
)

result_label.pack(pady=10)


app.mainloop()