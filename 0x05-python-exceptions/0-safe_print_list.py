#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if x:
        try:
            length = 0
            for item in my_list:
                length += 1
            if x > length:
                x = length
            for i in range(x):
                print(my_list[i], end="")
            print()
            return (x)
        except ValueError as e:
            print("Invalid value input", e)
        except TypeError as e:
            print("Incompatible type of data")
        except Exception as e:
            print("Something went wrong", e)
    else:
        print("Argument value not found")
