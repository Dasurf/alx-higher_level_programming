#!/usr/bin/python3

def search_replace(my_list, search, replace):
    string = str(my_list)
    if search in string:
        string.replace(search, replace)
        return string