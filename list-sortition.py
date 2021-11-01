# Objective: make a program that reads a list and shows the order drawn

import random

print('Enter your raffle list:\n')
item_1 = str(input('First item list: '))
item_2 = str(input('Second item list: '))
item_3 = str(input('Third item list: '))
item_4 = str(input('Fourth item list: '))
sortition = [item_1, item_2, item_3, item_4]
random.shuffle(sortition)
print('The random order of your list is: ')
print(sortition)
