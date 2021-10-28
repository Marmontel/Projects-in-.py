# Objective: Convert km to meters, centimeters to millimeters and micrometers.

meters = float(input('How many meters is your route? '))
centimeters = meters * 100
millimeters = meters * 1000
kilometers = meters / 1000
micrometers = meters * 1000000
print('Your route will have {}KM, {} meters, {} centimeters and {} milimeters'.format(
    kilometers, meters, centimeters, millimeters))
