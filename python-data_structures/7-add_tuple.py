#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    if len(ta) == 1:
        ta.append(0)
    elif len(ta) < 1:
        return tuple_b
    if len(tb) == 1:
        tb.append(0)
    elif len(tb) < 1:
        return tuple_a
    new_tuple = []
    new_tuple.append(ta[0] + tb[0])
    new_tuple.append(ta[1] + tb[1])
    return tuple(new_tuple)
