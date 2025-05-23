#Read the price of a product and give it a 5% discount
price = float(input('Type the product price: $'))

print('The price was ${:.2f} and after the 5% discount is ${:.2f}'.format(price, price*0.95))
print('You saved ${:.2f}'.format(price*0.05))