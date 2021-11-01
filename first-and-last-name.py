# Objective: Read full name and display first and last name

name = input(str('Write your full name'))
division = name.split()
print('Your first name is: {}'.format(division[0]))
print('Your last name is: {}'.format(division[-1]))
