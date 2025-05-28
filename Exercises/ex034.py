#Receive a salary and give a bonus
#If the salary is greater than R$1.250,00 give 10%
#If it is less than 15%

salary = float(input("Enter the salary: "))

print("The salary was R$ {:.2f}".format(salary))

print("After the bonus, it went up to R$", end = ' ')

print("{:.2f}.".format(salary * 1.1) if salary > 1250 else "{:.2f}".format(salary * 1.15))