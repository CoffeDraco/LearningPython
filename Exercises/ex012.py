#Read a salary and give it a 15% bonus
sal = float(input('Type the current salary: '))

print('The current salary is US$ {:.2f}. '
      'After a 15% bonus, it will be US${:.2f}!'.format(sal, sal*1.15))