#receive a full name and display the first and last name
full_name = str(input('Type a full name: '))

name_parts = full_name.split()
#last_name_pos = len(name_parts)-1

print("First Name:", name_parts[0])
#print("Last Name:", name_parts[last_name_pos])

#optimized
print("Last Name:", name_parts[-1])