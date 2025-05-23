#read a number in meters and convert to cm and mm
n = float(input('Type your height in meters: '))

print('You height is {:.2f} m, '
      'but you can also say that '
      'you have {:.0f} cm or {:.0f} mm'.format(n, n*100, n*1000))

