#!/usr/bin/python3

if __name__ == "__main__":

    thisList = [6, 7, 2, 8]

    def print_reversed_list_integer(my_list=[]):
        my_list.reverse()
        return my_list
    print(print_reversed_list_integer(thisList))