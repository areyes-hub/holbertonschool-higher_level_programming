#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition = 0
    arg_len = len(sys.argv)
    for num in range(1, arg_len):
        addition += int(sys.argv[num])
        print(addition)
