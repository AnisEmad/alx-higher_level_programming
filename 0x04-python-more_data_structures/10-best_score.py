#!/usr/bin/python3
def best_score(a_dictionary):
    mx = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > mx:
            mx = a_dictionary[i]
            name = i
    return name
