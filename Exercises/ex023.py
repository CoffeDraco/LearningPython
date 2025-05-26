#receive a four digit number and show every single digit of it
from turtledemo.forest import doit2

number = int(input('Type a number: '))

#mathematic way
d4 = number % 10
d3 = (number // 10) % 10
d2 = (number // 100) % 10
d1 = (number // 1000) % 10

print('\nMathematical way')
print('Unit: {}\nTens: {}\nHundreds: {}\nThousands: {}'.format(d4, d3, d2, d1))

#string way, works only with a full four number digits
#print('\nString way')
#number_string = str(number)
#print('Unit: {}\nTens: {}\nHundreds: {}\nThousands: {}'.format(number_string[3], number_string[2], number_string[1], number_string[0]))
