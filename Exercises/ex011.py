#read the dimensions of a wall (width and height), calculate the area
#and tell how much tint will be needed to paint it (2m² = 1L of tint)

w = float(input('Type the width of the wall: '))
h = float(input('Type the height of the wall: '))

area = w * h
wall_paint = area / 2

print('The area of your wall is {:.2f} m² '
      'and you will need {:.1f} L of wall paint to paint it.'.format(area, wall_paint))
