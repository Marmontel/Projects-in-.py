# Objective: Write a program that reads two integers and
# Compare them, showing on the screen a message:
# - The first value is greater
# - The second value is greater
# - There is no greater value, the two are equal

num_1 = int(input('Enter a integer number: '))
num_2 = int(input('Enter other integer number: '))
if num_1 > num_2:
    print('The FIRST value is greater!')
elif num_2 > num_1:
    print('The SECOND value is greater!')
else:
    print('There is no greater value, the two are equal')
