#Receive a name and if it meets the conditions, say something nice
name = str(input('Type your first name: '))

if len(name) <= 5:
    print("{} has such a nice ring to it".format(name))
else:
    print("{} is too long, I hope you have a nickname\nAnyway...".format(name), end=' ')

print("Good day to you", name)