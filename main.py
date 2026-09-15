import customtkinter as ctk
from gcd import gcd
from extended_gcd import extended_gcd

app = ctk.CTk()
app.title("GCD Calculator")
app.geometry("500x500")

#taking numbers as input and calculating gcd using gcd function 
def calculate_gcd():
    try : 
        a = int(first_number.get())
        b = int(second_number.get())

        result = gcd(a, b)
        result_label.configure(text=f"GCD = {result}")
    except ValueError:
        result_label.configure(text="Please enter valid integers")

#taking numbers as input and calculating extended gcd using extended gcd function
def calculate_extended_gcd():
    try:
        a = int(first_number.get())
        b = int(second_number.get())

        result, x, y = extended_gcd(a, b)

        result_label.configure(
            text=f"GCD = {result}\nx = {x}\ny = {y}"
        )

    except ValueError:
        result_label.configure(
            text="Please enter valid integers"
        )

#first number 
label_first = ctk.CTkLabel(
    app,
    text="First Number"
)
label_first.pack(pady=10)

#input box for first number 
first_number = ctk.CTkEntry(
    app,
    width=350,
    height=40
)
first_number.pack(pady=10)

#second number
label_second = ctk.CTkLabel(
    app,
    text="Second Number"
)
label_second.pack(pady=10)

#input box for second number 
second_number = ctk.CTkEntry(
    app,
    width=350,
    height=40
)
second_number.pack(pady=10)

#calcuate gcd button 
gcd_button = ctk.CTkButton(
    app,
    text="Calculate GCD",
    command=calculate_gcd
)
gcd_button.pack(pady=20)

#calculate extended gcd button
extended_gcd_button = ctk.CTkButton(
    app,
    text="Calculate Extended GCD",
    command=calculate_extended_gcd
)
extended_gcd_button.pack(pady=10)

#result box
result_label = ctk.CTkLabel(
    app,
    text="Result = "
)
result_label.pack(pady=10)

app.mainloop()