# Objective: Make a program that calcules the sum of all the
# odd numbers that are multiples of 3 and that lie in the range
# from 1 to 500.

sum = 0
count = 0
for odd in range(1, 501 2):
    if odd % 3 == 0:
        sum += odd
        count += 1
print('The sum of all {} requested values is {}.'.format(count, sum))
