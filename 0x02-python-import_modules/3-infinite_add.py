#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argLen = len(sys.argv)
    result = 0
    if (argLen + 1 == 1):
        print(sys.argv[1])
    elif (argLen + 1 >= 2):
        for i in range(argLen - 1):
            result += int(sys.argv[i + 1])
    print("{:d}".format(result))
