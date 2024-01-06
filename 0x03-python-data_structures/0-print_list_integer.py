#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

def print_list_integer(my_list=[]):
    for i in my_list:
        print("{}".format(i))
