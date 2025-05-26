text = 'Curso em Video Python'
print(text)

#simple slice method - string[start at : until_end+1 : pace]
#until_end+1 because the last one isn't counted

print('Sliced Text with text[5:13:2]\nStarting at 5 until 13 pace 2:',text[5:13:2])

#len returns the size of the string
print('\nString Size with len(text):', len(text))

#text.count('') counts how many times a 'determined_text'
#or character shows up in the string
print("\nThe letter 'o' shows up {} time(s) based on text.count('o')".format(text.count('o')))

#.count() can also be sliced, text.count('o', 0, 13)
#('determined_text', start at, until_end+1)

#.find() returns the position of a determined text
#if .find() doesn't find the text, it returns -1
print("\nThe text 'deo' is located at,", text.find('deo'), "based on text.find('deo')")

#Using the operator 'in'
print("\nIs 'curso' in text? ", 'curso' in text)

#.replace('determined_text', 'another_text'), it, as the name suggests, replace the text
print("\nNow is android, {}".format(text.replace('Python', 'Android')))

#.upper() transforms everything into uppercase
print('\nUppercase:', text.upper())

#.lower() transforms everything into lowercase
print('\nLowercase:', text.lower())

#.capitalize() turns the first letter into uppercase and the rest into lowercase
print('\nCapitalize:', text.capitalize())

#.title() turns every first letter in uppercase
print('\nTitle:', text.title(), end='\n\n')

#.strip() removes all the spaces from the beginning and ending of a text
#.rstrip() removes all spaces at the end
#.lstrip() removes all space at the beginning

#.split() it divides the string at every delimitator, usually spaces
splitted = text.split(' ')
print(splitted, end = '\n\n')

# ' '.join(string), it mesh together a splitted string with a chosen separator
joined = '-'.join(splitted)
print(joined, end = '\n\n')

#print("""Can be used to write multiple lines of text, but it breaks the line""")
print("""Texto com
Multiplas
linhas""")





