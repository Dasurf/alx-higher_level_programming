#!/usr/bin/python3

def multiple_returns(sentence):
    tolist = list(sentence)
    tostr = ''.join(map(str, tolist))
    strlen = len(tostr)
    return strlen, tostr[0]
