#!/usr/bin/python3

def no_c(my_string):
    arr = list(my_string)
    for i in arr:
        if i == 'c' or i == 'C':
            arr.remove(i)
            my_string = ''.join(map(str, arr))
    return my_string

