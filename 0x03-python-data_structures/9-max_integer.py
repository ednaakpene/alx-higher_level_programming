#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        maxi = my_list[0]
        for e in range(len(my_list)):
            if my_list[e] > maxi:
                maxi = my_list[e]
        return maxi
