#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for e in range(len(list(my_list))):
        if list(my_list)[e] == search:
            list(my_list)[e] = replace
    return list(my_list)
