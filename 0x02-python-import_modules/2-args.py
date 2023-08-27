#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("0 arguments.")
        sys.exit()
    elif arg_count == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count - 1))
    for i in range(1, arg_count):
        print("{}: {}".format(i, sys.argv[i]))
