# Objective: Write a program that reads the speed of a car
# If he goes over 80km/h, show a message saying he's been fined.
# The fine will cost $7,00 for each KM over the limit

speed = int(input('How fast was the car? '))
if speed > 80:
    print('You have exceeded the speed limit! And he will be fined ${}, for being {}KM/h above the 80Km/h allowed by law.'.format((speed - 80) * 7, speed - 80))
else:
    print('You are within the speed limit allowed by law and will not be fined!')
