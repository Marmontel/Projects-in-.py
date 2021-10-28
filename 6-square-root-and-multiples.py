# Objective: Show the double, triple and square root of a number

number = int(input('Write number: '))
double = number*2
triple = number*3
root = number**(1/2)
print('The double of {} is {}.\nThe triple is {}.\nAnd the square root is {:.2f}.'.format(
    number, double, triple, root))
