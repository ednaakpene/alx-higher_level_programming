#!/usr/bin/python3
def no_c(my_string):
    new1 = my_string.translate({ord("c"): None})
    new2 = new1.translate({ord("C"): None})
    return new2
