#Accessing Python Dictionary Using for loop
my_dict = {'a':'Python','b':'Javascript','c':'Golang'}

for key, value in my_dict.items():#Accessing both key and value using items()
	print(key, value)

for key in my_dict:#Accessing both key and value without using items()
	print(key,my_dict[key])

#Accessing both key and value using iteritems()
for key, value in my_dict.iteritem():#[doesnt work in python3]
	print(key, value)

for key in my_dict.keys():#Returning keys explicitly
    print(key)

for value in my_dict.values():#Returning values explicitly
    print(value)
