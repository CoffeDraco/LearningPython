#Receive a year and tell if it is a leap year
year = int(input("Type a year: "))

if year % 4 ==0:
    print("It is a leap year.")
else:
    print("Boohoo, it is a normal year.")
