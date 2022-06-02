#!/usr/bin/python3
for ac_num in range(122, 96, -1):
    if ac_num % 2 == 1:
        ac_num = ac_num - 32
    print("{:c}".format(ac_num), end='')
