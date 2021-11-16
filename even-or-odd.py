# Objective: Create a program that reads a number and says if it is even or odd

num = int(input('Enter a number to find out if it is odd or even: '))
rest = num % 2

if rest == 0:
    print('{} is a number even.'.format(num))
else:
    print('{} is a number odd.')
