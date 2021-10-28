# Objective: Create a program that reads the primitive type of the string

str = input('Write something: ')
print('The primitive type of this value is: ', type(str))
print('Only have spaces: ', str.isspace())
print('Is it a number? ', str.isnumeric())
print('Is it alphabetical? ', str.isalpha())
print('Is it alphanumeric? ', str.isalnum())
print('Is it upper? ', str.isupper())
print('Is it lower? ', str.islower())
print('Is it captalized? ', str.istitle())
