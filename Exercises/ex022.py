#Receive a complete name and show it in uppercase and lowercase,
#show how many characters it has (spaces not included)
#and show how many letters the first name has

full_name = str(input('Type a full name: ')).strip()

print('Uppercase:', full_name.upper())
print('Lowercase:', full_name.lower())
print('It has {} characters without spaces.'.format(len(full_name)-full_name.count(' ')))

splitted_name = full_name.split()
first_name = splitted_name[0]

print('The first name {} has {} characters.'.format(first_name, len(first_name)))

#another solution
#It will count how many characters until the first space
#print('The first name {} has {} characters.'.format(first_name, full_name.find(' ')))


