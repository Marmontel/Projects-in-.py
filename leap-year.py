# Objective: Make a program that reads any year and shows it's a leap

year = int(input('Enter a year to find out whether or not it is a leap year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('This is a leap year.')
else:
    print('This is not a leap year.')
