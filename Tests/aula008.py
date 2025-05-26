#import math
import random
from math import sqrt

num = int(input('Type a number: '))

sqrt_num = sqrt(num)
random_num = random.randint(1, 10)*num

print('The square of {} is {:.4f}.'.format(num, sqrt_num))
print('A random number using the typed one in the process: {}.'.format(random_num))
print("😀")

