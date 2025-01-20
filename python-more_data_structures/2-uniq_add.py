#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    uniq_sum = 0
    for n in uniq:
        uniq_sum += n
    return uniq_sum
