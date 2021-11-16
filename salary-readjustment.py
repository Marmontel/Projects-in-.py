# Objective: Write a program that asks for an employee's salary and calculates his raise.
# For salaries greater than $1.250, calculate a 10% increase.
# For less than or equal to the increase is 15%

salary = int(input('What is your salary? $'))
readjustment = salary + (salary * 0.10)
readjustment_2 = salary + (salary * 0.15)

if salary >= 1250:
    print('Your readjustment will be 10%. With the readjustment, your salary becomes: {:.2f}'.format(
        readjustment))
else:
    print('Your readjustment will be 15%. With the readjustment, your salary becomes: {:.2f}'.format(
        readjustment_2))
