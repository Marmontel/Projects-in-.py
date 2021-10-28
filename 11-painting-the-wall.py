# Objective: make a program that reads the width and height of a
# wall in meters. Calculate your area and the amount of paint needed
# to paint it. Knowing that 1 liter of paint paints 2m squares.

width = float(input('How wide is the wall? '))
height = float(input('How height is the wall? '))
diameter = width*height
print('Its wall is {}x{} dimension and its area is {}m².'.format(
    width, height, (width*height)))
print('To paint the wall you will need {}L of paint.'.format(diameter/2))
