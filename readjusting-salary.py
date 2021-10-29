# Objective: make an algorithm that reads an
# employee´s salary and show your new salary with a 15% increase.

salary = float(input('What is the salary employee´s? $'))
increase = salary + (salary * 15 / 100)
print('An employee who earned ${:.2f}, with a 15% increase starts receiving ${:.2f}'.format(
    salary, increase))
