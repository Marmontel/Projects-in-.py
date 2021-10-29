# Objective: Convert Real (R$) currency to Dollar ($)

real = float(input('What is the value in Real in your wallet? R$'))
dollar = real / 5.54
print('With R${} you buy ${:.2f}.'.format(real, dollar))
print('Quote at R$5,54 of day 27/10/2021.')
