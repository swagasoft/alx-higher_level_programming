#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
