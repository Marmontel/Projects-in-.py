# Objective: Write a program to approve the bank loan for a home purchase.
# The program will ask:
# The house value;
# Buyer's salary;
# In how many years will he pay;
# NOTE: The program cannot exceed 30% of the buyer's salary

print('=~'*20)
print('SIMULADOR DE EMPRÉSTIMOS.')

# House value
house_value = float(input('What is the value of the house: R$'))
# Buyer Salary
salary = float(input('Buyer salary: R$'))
# Years of financing
financing = int(input('How many years of financing: '))
# 30% of salary
percentage_salary = salary * 0.3
# Installments
installment = house_value / (financing * 12)

print('To pay a house of ${:.2f} in {} years, the installment will be ${:.2f}.'.format(
    house_value, financing, installment))

# If the value of the house installments exceeds 30% of the salary, then print DENIED
if percentage_salary < installment:
    print('FINANCING DENIED!')
# If it does not exceed, then print APPROVED
else:
    print('FINANCING APPROVED!')
print('=~'*20)
