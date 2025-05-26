#Receive the opposite and adjacent side of a triangle and
#calculate the hypotenuse

from math import hypot

opp_side = float(input('Type the opposite side: '))
adj_side = float(input('Type the adjacent side: '))

#hi = (opp_side ** 2 + adj_side ** 2) ** (1/2) #manual mode
hi = hypot(opp_side, adj_side)

print('The hypotenuse is {:.4f}.'.format(hi))

