#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [True if x % 2 == 0 else False for x in my_list]
    return result
