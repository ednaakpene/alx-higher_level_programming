#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    nr = 0
    dr = 0
    for val, weight in my_list:
        nr += val * weight
        dr += weight
    return (nr / dr)
