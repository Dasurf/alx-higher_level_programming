#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = 0
    if my_list:
        for i in my_list:
            if i > temp:
                temp = i
        return temp
    else:
        return None
