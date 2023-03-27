#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = a / b
    except (ZeroDivisionError, FloatingPointError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return answer
