#!/usr/bin/python3
def check_input(string):
    for i in string:
        if i not in 'MCDLXVI':
            return False
    return True


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not check_input(roman_string):
        return 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    num = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if dict[roman_string[i]] < dict[roman_string[i + 1]]:
                num -= dict[roman_string[i]]
            else:
                num += dict[roman_string[i]]
        else:
            num += dict[roman_string[i]]
    return num
