#Receive a distance and calculate the price of the ticket
#Until 200 km it's R$0,50 per km, over it is R$0,45

distance = float(input("Type the distance: "))

print("The price of the ticket is R$", end=" ")

print("{:.2f}".format(distance * 0.50 if distance <= 200 else distance * 0.45))