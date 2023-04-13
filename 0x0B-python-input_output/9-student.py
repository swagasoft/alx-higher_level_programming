#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """ Student class body."""

    def __init__(self, first_name, last_name, age):
        """Initialize student props in contructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
