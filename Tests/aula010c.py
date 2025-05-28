#Receive two scores from a student and give some feedback
#A good score is (n1+n2)/2 >= 5

n1 = float(input("Type the first score: "))
n2 = float(input("Type the second score: "))

m = (n1 + n2) / 2

#simplified method
print("Congratulations, you've passed with {:.2f}!".format(m) if m>=5 else "Shame on you and your score of {:.2f}.".format(m))