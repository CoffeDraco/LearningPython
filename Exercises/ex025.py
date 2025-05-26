#receive a name and say if it contains the word "SILVA"
full_name = str(input('Type a full name: ')).strip()

print("The name {} contains 'SILVA' in it?".format(full_name), 'SILVA' in full_name.upper())
