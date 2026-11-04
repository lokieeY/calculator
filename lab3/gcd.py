from operations import *

def mod(a,b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    if b=="0":
        return "Invalid"
    quotient = divide(a,b)
    product = multiply(quotient,b)
    remainder = subtract(a,product)
    return remainder.lstrip("0") or "0"


def gcd(a,b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    while b != "0":
        r = mod(a,b)
        a=b
        b=r
    return a


# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b

#     return a