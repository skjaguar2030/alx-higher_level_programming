#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % -10 if number < 0 else number % 10
if(last > 5):
    print(F'Last digit of {number:d} is {last:d} and is greater than 5')
elif(last == 0):
    print(F'Last digit of {number:d} is {last} and is 0')
else:
    print(F'Last digit of {number:d} is {last} and is less than 6 and not 0')
