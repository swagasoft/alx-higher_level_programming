#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Square class body."""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the new area of the square."""
        return (self.__size * self.__size)
