def function_sub(a, b):
    return a - b


def function_mul(a, b):
    return a * b


def function_div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def is_even(number):
    return number % 2 == 0


def concat_strings(a, b):
    return f"{a}{b}"


class Fuction:
    pass