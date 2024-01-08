#!/usr/bin/python3

def multiple_returns(sentence):
    tolist = list(sentence)
    tostr = ''.join(map(str, tolist))
    strlen = len(tostr)
    if strlen == 0:
        return 0, "None"
    return strlen, tostr[0]
