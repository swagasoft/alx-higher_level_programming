#!/usr/bin/python3
"""A class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        Boolean of an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
