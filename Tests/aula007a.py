#name = str(input('What is your name? '))
#print('Hi there {:_^20}!'.format(name))
#____name____ will have a limit of 20 and have empty spaces filled with underline

a = int(input('Type a number: '))
b = int(input('Typer another number: '))

print('The sum is {}, \nthe product is {} and \nthe division is {:.5f}'.format(a+b, a*b, a/b), end='\n\n')

