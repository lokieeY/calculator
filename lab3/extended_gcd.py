from operations import *

class SignedNumber:
    def __init__(self, value, negative=False):
        self.value = value
        self.negative = negative
def signed_to_string(number):
    if number.negative:
        return "-" + number.value

    return number.value

def subtract_signed(a, b):
    # Different signs
    if a.negative != b.negative:
        value = add(a.value, b.value)
        return SignedNumber(value, a.negative)

    # Same signs
    cmp = compare(a.value, b.value)

    # Equal values
    if cmp == 0:
        return SignedNumber("0", False)

    # |a| > |b|
    if cmp == 1:
        value = subtract(a.value, b.value)
        return SignedNumber(value, a.negative)

    # |b| > |a|
    value = subtract(b.value, a.value)
    return SignedNumber(value, not a.negative)


def extended_gcd(a, b):
    # Remainders
    old_r = a
    r = b

    # Coefficients of a
    old_s = SignedNumber("1")
    s = SignedNumber("0")

    # Coefficients of b
    old_t = SignedNumber("0")
    t = SignedNumber("1")

    while r != "0":
        # q = old_r / r
        q = divide(old_r, r)

        # Calculate new remainder
        qr = multiply(q, r)
        new_r = subtract(old_r, qr)

        # Calculate new s
        qs = multiply(q, s.value)
        temp_s = SignedNumber(qs, s.negative)
        new_s = subtract_signed(old_s, temp_s)

        # Calculate new t
        qt = multiply(q, t.value)
        temp_t = SignedNumber(qt, t.negative)
        new_t = subtract_signed(old_t, temp_t)

        # Update values
        old_r = r
        r = new_r

        old_s = s
        s = new_s

        old_t = t
        t = new_t

    return old_r, old_s, old_t



# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0

#     gcd, x1, y1 = extended_gcd(b, a % b)

#     x = y1
#     y = x1 - (a // b) * y1

#     return gcd, x, y