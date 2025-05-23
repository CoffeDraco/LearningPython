#Receive the amount of kilometers traveled by a rental car and in how many days
#Then calculate the expenses, knowing that is R$60,00/day and R$0,15/Km

tkm = int(input('Type the amount of Km traveled: '))
days = int(input('Type how many days you traveled with the car: '))

print('\nPrepare you wallet! You will pay R${:.2f}.'.format(tkm * 0.15 + days * 60))
print('\nDetailed pricing:\n'
      '- For the distance traveled = R${:.2f}\n'
      '- For the amount of days = R${:.2f}.'.format(tkm * 0.15, days * 60))