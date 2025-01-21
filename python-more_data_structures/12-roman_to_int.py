#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_chars = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    invalid_repetition = {"V", "L", "D"}
    prev_char = ""
    repeat_count = 0
    for i in range(len(roman_string)):
        char = roman_string[i].upper()
        if char not in rom_chars:
            return "Invalid roman numeral"

        if char == prev_char:
            repeat_count += 1
            if char in invalid_repetition or repeat_count >= 3:
                return "Invalid roman numeral"
        else:
            repeat_count = 0
        prev_char = char

    num = 0
    i = 0
    while i < len(roman_string):
        curr_val = rom_chars[roman_string[i].upper()]
        if i + 1 < len(roman_string):
            next_val = rom_chars[roman_string[i + 1].upper()]
            if curr_val < next_val:
                num += (next_val - curr_val)
                i += 1
            else:
                num += curr_val
        else:
            num += curr_val
        i += 1
    return num
