# Objective: Write a program that reads any integer
# And ask the user to choose which conversion base will be

print('~='*20)
print('NUMERIC BASE CONVERTER')

number = int(input('Enter an integer number: '))
print('''CHOOSE ONE OF THE BASES FOR CONVERSION:
[ 1 ] Converter to BINARY
[ 2 ] Converter to OCTAL
[ 3 ] Converter to HEXADECIMAL
''')
option = int(input('Enter your option: '))
if option == 1:
    print('{} converted to BINARY is equal to {}.'.format(
        number, bin(number)[2:]))
elif option == 2:
    print('{} converted to OCTAL is equal to {}.'.format(
        number, oct(number)[2:]))
elif option == 3:
    print('{} converted to HEXADECIMAL is equal to {}.'.format(
        number, hex(number)[2:]))
else:
    print('INVALID OPTION! Try again.')
print('~='*20)
