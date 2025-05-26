#Receive a city name and say if it starts with the word "SANTO"

city_name = str(input('\nType a city name: ')).strip().upper()

#First Solution
split_city_name = city_name.split()
print('The city name starts with "SANTO"?', 'SANTO' in split_city_name[0])

#Another Solution
print('The city name starts with "SANTO"?', city_name[:5] == "SANTO")