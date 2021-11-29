# Objective: Create a progam that calculates the amount to be paid for a product considering
# Regular price and payment terms
# - Cash view: 10% discount
# - Cash on the card: 5% discount
# - Up to 2 installments on the card: Normal price
# - 3x or more on the card: 20% interest

print('='*11, 'STORE BRAZIL', '='*11, '\n')
price = float(input('Total value of purchase: $'))
print('''PAYMENTS METHODS:
[ 1 ] Cash with 10% discount.
[ 2 ] Cash on debit card with 5% discount.
[ 3 ] In up to 2x interest-free installments on your credit card.
[ 4 ] 3x or more on the card with 20% surcharge.
''')
option = int(input('Enter the desired payment option: '))
if option == 1:
    cash = price - (price * 0.10)
    print('Paying in cash you get 10% off! From ${:.2f} the product starts to cost ${:.2f}!'.format(
        price, cash))
elif option == 2:
    debit = price - (price * 0.05)
    print('Paying with a cash debit you get a 5% discount! From ${:.2f} the product starts to cost ${:.2f}!'.format(
        price, debit))
elif option == 3:
    print('Pay in 2x ${:.2f} on your credit card. There are no discounts.'.format(
        price / 2))
elif option == 4:
    interest = price + (price * 0.2)
    print('Paying in 3x or more you will get 20% surcharge! From ${:.2f}, the product will cost ${:.2f}'.format(
        price, interest))
else:
    print('INVALID OPTION! TRY AGAIN.')
print('~='*20)
