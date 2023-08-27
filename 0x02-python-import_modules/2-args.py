#!/usr/bin/python3
import sys
if __name__ == "__main__":
	len = len(sys.argv)
	if len == 1:
		print("0 arguments.")
		sys.exit()
	elif len == 2:
		print("1 argument:")
	else:
		print("{} arguments:".format(len - 1))
	for i in range(1, len):
		print("{}: {}".format(i, sys.argv[i]))
