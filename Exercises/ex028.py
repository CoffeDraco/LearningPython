#Sort out a random number and ask the user to type one as well
#between 0 and 5. If both are the same, congratulate the user

from random import randint

random_number = randint(1, 5)

user_number = int(input("Type a number between 1~5: "))

print("Yeah, You Won!" if user_number == random_number else "Nope, You Lose!")