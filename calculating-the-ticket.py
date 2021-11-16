# Objective: develop a program that asks the distance of a journey in km.
# Calculate the ticket price, charging $0.50 per km for trips up to 200km and $0.45 per km for longer trips

km = float(input('What is the travel distance in KM? '))
ticket = km * 0.5
if km > 200:
    ticket = km * 0.45
print('The value of your ticket is: {}'.format(ticket))

