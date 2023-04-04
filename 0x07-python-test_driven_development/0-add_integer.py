
#!/usr/bin/python3

"""0-add_integer
The function "add_integer"  returns the sum of two integers.
"""
def add_integer(a, b=98):
    """adds two integers function body"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
