#Receive a float number a show just the integer part
#from math import floor
from math import trunc

num = float(input('Type a number: '))
#print('The integer part is {:.0f}.'.format(floor(num)))
print('The typed number is {} and its integer part is {}.'.format(num, trunc(num)))