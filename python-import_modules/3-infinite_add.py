#!/usr/bin/python3
import sys

addition = 0
arg_len = len(sys.argv)
for num in range(1, arg_len):
        addition += int(sys.argv[num])
print(addition)
