#Read a number and show its double, triple and square
num = int(input('Type a number: '))

print('You typed', num)
print('Its double value is {} \nIts triple value is {}'.format(num*2, num*3))
print('And its square value is', pow(num,1/2), end='\n\n')
print('Finish line')

