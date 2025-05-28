#Receive the speed of a car
#If it's over 80, tell the user that he will be fined
#and will pay R$7,00 per km above the speed limit

speed = float(input("Type the speed of the car: "))

if speed <= 80:
    print("You're OK, keep going!")
else:
    infraction_value = (speed -80) * 7
    print("Oh well, you didn't respected the speed limit and will pay R${:.2f}.".format(infraction_value))