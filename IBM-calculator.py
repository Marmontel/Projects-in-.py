# Objective: Create a program that reads a person's height and weight and calculates
# Your BMI and show your status according to the table below
# - Under 18.5: Underweight
# - Between 18.5 and 25: Ideal weight
# - 25 to 30: Overweight
# - 30 to 40: Obesity
# - Over 40: Morbid Obesity

print('\n')
print('~='*20)
print('*/*\*CALCULATE YOUR BMI*/*\*')

weight = float(input('Enter your weight (in KG): '))
height = float(input('Inform your height (in Meters): '))
bmi = weight / (height**2)
print('Your BMI is: {:.1f}'.format(bmi))
if bmi <= 18.5:
    print('You are UNDER WEIGHT.')
elif bmi <= 25:
    print('You are at your NORMAL WEIGHT.')
elif bmi <= 30:
    print('You are OVERWEIGHT.')
elif bmi <= 40:
    print('You are OBESE')
else:
    print('You are MORBIDLY OBESE')
print('=~'*20)
