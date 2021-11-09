# Objective: To write a program that thinks of an integer between 0 and 5 and ask the
# User to try to find out which number was chosen by the computer
# The program should write on the screen if the user won or lost

import random

num = int(input('Test your luck! Write a number from 0 to 5: '))
sortition = random.randint(0, 5)
if num == sortition:
    print('Wow, today is your lucky day, you got it right!')
else:
    print("What a pity! It wasn't this time, try again!")
