#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = []
    for el in range(list_length):
        try:
            if el >= len(my_list_1) or el >= len(my_list_2):
                raise IndexError
            if not isinstance(my_list_1[el], (int, float)) or not isinstance(my_list_2[el], (int, float)):
                raise TypeError
            if my_list_2[el] == 0:
                raise ZeroDivisionError
            division.append(my_list_1[el] / my_list_2[el])
        except ZeroDivisionError:
            division.append(0)
            print("division by 0")
        except TypeError:
            division.append(0)
            print("wrong type")
        except IndexError:
            division.append(0)
            print("out of range")
    return division
