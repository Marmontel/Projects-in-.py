# Objective: make a program that reads the lenght of the opposite leg and the
# adjacent side of a rectangular triangle.
# Calculate and show the length of the hypotenuse.

from math import hypot
opposite = float(input('Length of opposite leg: '))
adjacent = float(input('length of adjacent leg: '))
print('The hypotenuse will measure: {:.2f}'.format(hypot(opposite, adjacent)))
