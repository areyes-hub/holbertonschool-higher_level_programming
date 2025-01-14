#!/usr/bin/python3
for nums in range(0, 80):
    if (nums % 10) > (nums // 10) and nums != 89:
        print("{:02}, ".format(nums), end="")
print("89")
