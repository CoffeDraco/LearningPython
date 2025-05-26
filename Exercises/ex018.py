#receive an angle and print the sine, cosine e tangent of it
from math import sin, cos, tan, radians

angle = float(input('Type an angle: '))

#angle in radians is angle*pi/180
angle_radians = radians(angle)

#These functions works with the angle in radians
sin = sin(angle_radians)
cos = cos(angle_radians)
tan = tan(angle_radians)

print('The typed angle is {:.2f}º'.format(angle))
print('Its sine is {:.2f}'.format(sin))
print('Its cosine is {:.2f}'.format(cos))
print('Its tangent is {:.2f}'.format(tan))



