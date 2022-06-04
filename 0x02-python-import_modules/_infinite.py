#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    number_of_arguments = len(argv) - 1
    if number_of_arguments > 0:
        result = []
        for i in range(1, number_of_arguments + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result)))
    else:
        print("{}".format(number_of_arguments))
