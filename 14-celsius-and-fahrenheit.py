# Objective: Convert Celsius degrees to Fahrenheit

def menu():
    print('TEMPERATURE CONVERTER!\n', '-' * 12)
    print('1. Convert from Celsius to Fahrenheit.')
    print('2. Convert from Fahrenheit to Celsius.')


def cel_fahr():
    celsius = float(input('Temperature in °C: '))
    fahr = celsius * (9 / 5) + 32
    print('Temperature in °F: {:.2f}'.format(fahr))


def fahr_cel():
    fahrenheit = float(input('Temperature in °F: '))
    celsi = (fahrenheit - 32) * (5 / 9)
    print('Temperature in °C: {:.2f}'.format(celsi))


if __name__ == '__main__':
    menu()
    selection = input('Choose the type of conversion you what to perform.')
    if selection == '1':
        cel_fahr()

    if selection == '2':
        fahr_cel()
