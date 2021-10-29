# Objective: Create a program that reads any real number from the keyboard and
# show your entire portion on screen.

from math import trunc
number = float(input('Enter a value: '))
print('The value entered was {} and its entire portion is {}.'.format(
    number, trunc(number)))
