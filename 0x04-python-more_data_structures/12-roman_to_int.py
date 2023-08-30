#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    num = 0
    if isinstance(roman_string, str) or roman_string is None:
        return
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if dict[roman_string[i]] < dict[roman_string[i + 1]]:
                num -= dict[roman_string[i]]
            else:
                num += dict[roman_string[i]]
        else:
            num += dict[roman_string[i]]
    return num
