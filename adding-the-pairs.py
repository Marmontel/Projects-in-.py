# Objective: Develop a program that reads 6 numbers
# and show the sum only of those that are even
# and disregard the odd numbers

print('~='*20)
print('Enter six numbers and well just add the even numbers!')
sum = 0
count = 0
for numbers in range(1, 7):
    value = int(input('Enter the {} value: '.format(numbers)))
    if value % 2 == 0:
        sum += value
        count += 1
print('You entered {} even numbers and the sum of then is {}.'.format(count, sum))
print('~='*20)
