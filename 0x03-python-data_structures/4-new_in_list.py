#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = my_list.copy()
    if len(my_list) - 1 < idx or idx < 0:
        return b
    b[idx] = element
    return b
