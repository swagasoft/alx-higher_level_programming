#!/usr/bin/python3
"""Defines an inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.
    Returns:
        A boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
