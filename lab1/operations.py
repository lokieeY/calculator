#addition
def add(a, b):
    i = len(a) - 1
    j = len(b) - 1

    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry:

        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry

        result = str(total % 10) + result
        carry = total // 10

        i -= 1
        j -= 1

    return result


#compare
def compare(a, b):
    
    # Remove leading zeros
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"

    # Compare number of digits
    if len(a) > len(b):
        return 1

    if len(a) < len(b):
        return -1

    # Same number of digits
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1

        if a[i] < b[i]:
            return -1

    return 0


#subtract positive 
def subtract_positive(a, b):
    i = len(a) - 1
    j = len(b) - 1

    borrow = 0
    result = ""

    while i >= 0:

        digit_a = int(a[i]) - borrow
        digit_b = int(b[j]) if j >= 0 else 0

        if digit_a < digit_b:
            digit_a += 10
            borrow = 1
        else:
            borrow = 0

        difference = digit_a - digit_b

        result = str(difference) + result

        i -= 1
        j -= 1

    return result.lstrip("0") or "0"

#subtract
def subtract(a, b):
    
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"

    comparison = compare(a, b)

    if comparison == 0:
        return "0"

    if comparison < 0:
        return "-" + subtract_positive(b, a)

    return subtract_positive(a, b)


#multiplication
def multiply(a, b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"

    if a == "0" or b == "0":
        return "0"

    result = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):

            digit_a = int(a[i])
            digit_b = int(b[j])

            result[i + j + 1] += digit_a * digit_b

    for i in range(len(result) - 1, 0, -1):

        carry = result[i] // 10

        result[i] %= 10

        result[i - 1] += carry

    return ''.join(map(str, result)).lstrip("0") or "0"

#division 
def divide(a, b):
    
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"

    if b == "0":
        raise ValueError("Division by zero")

    if compare(a, b) < 0:
        return "0"

    quotient = ""
    current = "0"

    for digit in a:

        if current == "0":
            current = digit
        else:
            current = current + digit

        current = current.lstrip("0") or "0"

        quotient_digit = 0

        while compare(current, b) >= 0:
            current = subtract(current, b)
            quotient_digit += 1

        quotient += str(quotient_digit)

    return quotient.lstrip("0") or "0"