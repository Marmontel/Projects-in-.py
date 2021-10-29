# Objective: make an algorithm that reads the price of a product and displays
# your new price with 5% discount

price = float(input('What is the value of the product? R$'))
new_price = price - (price * 5 / 100)
print('The product that used to cost ${:.2f}, in the 5% discount promotion will cost ${:.2f}!'.format(
    price, new_price))
