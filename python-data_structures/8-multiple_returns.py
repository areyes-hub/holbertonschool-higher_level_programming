#!/usr/bin/python3
def multiple_returns(sentence):
    tup = [len(sentence) if len(sentence) > 0 else 0, sentence[0] if len(sentence) > 0 else None]
    return tuple(tup)
