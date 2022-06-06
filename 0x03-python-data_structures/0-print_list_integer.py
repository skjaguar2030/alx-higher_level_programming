#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # a function that print all intigers in a list passed as a parameter
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
