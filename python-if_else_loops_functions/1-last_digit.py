#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
last_num = num[-1]
if number < 0:
    last_num = f"{'-'}{last_num}"
    print(f"Last digit of {num} is {last_num} and is less than 6 and not 0")
elif number > 0:
    if number % 10 > 5:
        print(f"Last digit of {num} is {last_num} and is greater than 5")
    elif number % 10 < 6 and number % 10 > 0:
        print(f"Last digit of {num} is {last_num} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is {last_num} and is 0")
else:
    print(f"Last digit of {num} is {last_num} and is 0")
