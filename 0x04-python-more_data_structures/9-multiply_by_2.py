#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newd = a_dictionary.copy()
    list_keys = list(newd.keys())
    for e in list(newd.keys()):
        newd[e] *= 2
    return (newd)
