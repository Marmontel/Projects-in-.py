# Objective: Make a program that reads the year of birth
# of young and informed, according to their agr:
# - if he IS STILL GOING TO ENLIST for military service
# - If it's time to enlist
# - If the enlistment time has passed
# - How much time has passed / is missing the deadline

from datetime import date

today = date.today().year
birth = int(input('Year of birth: '))
old = today - birth
print('Who was born in {} is {} years old in {}'.format(birth, old, today))
if old == 18:
    print('You have to sign up IMMEDIATELY')
elif old < 18:
    missing = 18 - old
    print('You are not yet 18 years old. Still {} years to enlist.'.format(missing))
    years = today + missing
    print('Your enlistment will be in {}'.format(years))
elif old > 18:
    missing = old - 18
    print('You should have enlistment {} years ago.'.format(missing))
    years = today - missing
    print('Your enlistment was in {}'.format(years))
