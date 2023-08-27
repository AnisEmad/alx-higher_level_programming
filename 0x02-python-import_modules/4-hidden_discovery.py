#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    attributes = dir(hidden_4)
    attributes = sorted(attributes)
    for i in attributes:
        if i[0] != '_' and i[1] != '_':
            print(i)
