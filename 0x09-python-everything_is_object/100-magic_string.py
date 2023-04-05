#!/usr/bin/python3
def magic_string(times=[0]):
    times[0] = times[0] + 1
    return "BestSchool" + (", BestSchool" * (times[0] - 1))
