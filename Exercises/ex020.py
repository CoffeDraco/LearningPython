#Receive four names and randomize their order

from random import shuffle

name1 = str(input('Type the first name: '))
name2 = str(input('Type the second name: '))
name3 = str(input('Type the third name: '))
name4 = str(input('Type the fourth name: '))

names = [name1, name2, name3, name4]

shuffle(names)

print("The randomized presentation is: {}".format(names))
