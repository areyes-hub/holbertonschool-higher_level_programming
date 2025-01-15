#!/usr/bin/python3
import sys

arg_len = len(sys.argv)
count = 1
if arg_len < 2:
    print("{} arguments.".format(arg_len - 1))
elif arg_len == 2:
    print("{} argument.".format(arg_len - 1))
    print("{}: {}".format(arg_len - 1, sys.argv[1]))
else:
    print("{} arguments:".format(arg_len - 1))
    for arg in range(1, arg_len):
        print("{}: {}".format(count, sys.argv[arg]))
        count += 1
