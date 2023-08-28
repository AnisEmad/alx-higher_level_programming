#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        for item in my_list:
            if index < x:
                print(item, end="")
                index = index + 1
            else:
                break
        print("")
        return index
    except Exception as e:
        print(f"An error occurred: {e}")
