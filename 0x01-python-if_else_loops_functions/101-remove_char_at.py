#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ""
    for ch in str:
        if i != n:
            new_str += ch
        i += 1
    return 
