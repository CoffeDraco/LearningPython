#Receive three numbers and display the biggest and the smallest

n1 = float(input("Type the first number: "))
biggest_number = n1

n2 = float(input("Type the second number: "))
if n2 > biggest_number:
    biggest_number = n2
    smallest_number = n1
else:
    smallest_number = n2

n3 = float(input("Type the third number: "))
if n3 > biggest_number:
    biggest_number = n3
elif n3 < smallest_number:
    smallest_number = n3

print("The biggest number is:", biggest_number)
print("The smallest number is:", smallest_number)
