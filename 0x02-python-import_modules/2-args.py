#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argNum = len(sys.argv)
    if (argNum == 1):
        print("{} arguments".format(argNum - 1) + ".")
    elif (argNum == 2):
        print("{} argument".format(argNum - 1) + ":")
        print("{}:".format(1), sys.argv[1])
    elif (argNum > 2):
        print("{} arguments".format(argNum - 1) + ":")
        for i in range(argNum - 1):
            print("{}:".format(i + 1), sys.argv[i + 1])
