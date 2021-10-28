# Objective: Create annual or monthly interest calculations, giving freedom of choice.

def menu():
    print('Calculate your interest, choose one of the options: ')
    print('1. Calculate monthly interest.')
    print('2. Calculate annual interest.')


def month():
    value = float(input('What amount do you want to calculate interest on? $'))
    interest_month = float(input('Percentage of interest per month: '))
    interest = value + (value * interest_month / 100) - value
    month_interest = value + (value * interest_month / 100)
    print('The monthly interest rate is {:.2f}% per month.'.format(
        interest_month))
    print('Therefore, the amount charged in the addition per month must be: ${:.2f}'.format(
        interest))
    print('With monthly interest, the installment becomes: ${:.2f}.'.format(
        month_interest))
    print('Also resulting in ${:.3f} of interest per day.'.format(
        interest / 30))


def annual():
    value = float(input('What amount do you want to calculate interest on? $'))
    interest_annual = float(input('Percentage of interest per year: '))
    interest = value + (value * interest_annual / 100) - value
    annual_interest = value + (value * interest_annual / 100)
    print('The interest rate is ${:.2f} per year.'.format(interest_annual))
    print('Therefore, the amount of interest per month must be: ${:.2f}'.format(
        interest / 12))
    print('In one year the value of turns: ${:.2f}'.format(annual_interest))


if __name__ == '__main__':
    menu()
    selection = input('Choose which of the options you want to calculate: ')
    if selection == '1':
        month()

    if selection == '2':
        annual()
