# Objective: redo multiplication tables
# of a number the user chooses
# only now using for

number = int(input('Enter a number to find the multiplication table: '))
print('=~'*12)
print('*'*3, 'THIS IS THE TABLE OF {}'.format(number), '*'*3)
for multip in range(1, 11, 1):
    mult = number * multip
    print('{} x {:2} = {}'.format(number, multip, mult))
print('=~'*12)
