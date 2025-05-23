#read a celsius temperature and convert to fahrenheit
temp = float(input('Type the current temperature of your place in ºC: '))

fahrenheit = temp*9/5 + 32

print('You typed {:.1f} ºC, that is equivalent to {:.1f} ºF!'.format(temp, fahrenheit))
