# Objective: Create a program that reads 3 numbers and says which is the largest and which is the smallest

num = int(input('Enter a number: '))
num_2 = int(input('Enter other number: '))
num_3 = int(input('Enter one more number: '))
main = num
if (num_2 > num):
    main = num_2
if (num_3 > main):
    main = num_3
print('Biggest:', main)

smaller = num
if (num_2 < smaller):
    smaller = num_2
if (num_3 < smaller):
    smaller = num_3
print('Smaller:', smaller)
