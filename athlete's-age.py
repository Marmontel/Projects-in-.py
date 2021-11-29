# Objective: Create a program that reads as athlete's age and displays their age category
# - Up to 9 years old: MIRIM
# - Up to 14 years old: CHILDREN
# - Up to 19 years old: JUNIOR
# - Up to 20 years old: SENIOR
# - Above: MASTER

from datetime import date

today = date.today().year
birth = int(input('Year of birth: '))
old = today - birth
print('The athlete has {} years old.'.format(old))
if old <= 9:
    print('Category: MIRIM')
elif old <= 14:
    print('Category: CHILDREN')
elif old <= 19:
    print('Category: JUNIOR')
elif old <= 25:
    print('Category: SENIOR')
else:
    print('Category: MASTER')
