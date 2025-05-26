#Receive a sentence and say
#How many times the letter 'A' appear
#What is its first appearance position?
#What is its last appearance position?

sentence = str(input('Type a sentence: ')).strip().upper()

a_count = sentence.count('A')
a_first_pos = sentence.find('A')
a_last_pos = sentence.rfind('A')

print("The letter 'A' is used {} times.\n".format(a_count))
print('The first use is at the position {}.\n'.format(a_first_pos))
print('The last use is at the position {}.'.format(a_last_pos))
