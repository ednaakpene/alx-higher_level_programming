#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary)
    for e in sort:
        print("{}: {}".format(e, a_dictionary.get(e)))
