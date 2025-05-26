#Receive four names and choose one at random
from random import choice

name1 = str(input('First name: '))
name2 = str(input('Second name: '))
name3 = str(input('Third name: '))
name4 = str(input('Fourth Name: '))

lista = [name1, name2, name3, name4]

print('The names were: {}, {}, {}, {}'.format(name1, name2, name3, name4))
print('And the chosen one is: {}'.format(choice(lista)))

