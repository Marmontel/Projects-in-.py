# Write a program that asks for the amount
# of KM traveled by a rental car and the number of days he has been rented.
# Calculate the price to pay, knowing that the car costs $60/day and $0,15 per KM driven.

days = float(input('How many days rented? '))
km = float(input('How many KM run? '))
pay = (days * 60) + (km * 0.15)
print('The total to be paid is: ${}'.format(pay))
