#read a number about how much money in R$ a person has,
#and how many dollars can they buy with it
#consider this US$1,00 = R$3,27

wallet = float(input("Let's be blunt. \nType how much money you have in R$: "))

print('Well, with just R${:.2f}, you can buy a change worth of US${:.2f}'.format(wallet, (wallet / 3.27)))
