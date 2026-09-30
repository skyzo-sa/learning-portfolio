print('#' * 10 + ' DICTIONARY OPERATIONS AND METHODS - PART 1 ' + '#' * 10)
# DICTIONARY OPERATIONS AND METHODS - PART 1

person = {'name': 'John', 'age': 35, 'location':'Soweto'}

friend = person
person['name'] = 'Michael'
print(friend) # {'name': 'Michael', 'age': 35, 'location': 'Soweto'}

neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)

countries = {'ro': 'Romania', 'us': 'United States', 'de': 'Germany'}
countries.update({'hu': 'Hungary', 'ca': 'Canada', 'fr': 'France'})
print(countries)

person.clear()
print(person, friend) # {} {}


print('#' * 10 + ' DICTIONARY OPERATIONS AND METHODS - PART 2 ' + '#' * 10)
# DICTIONARY OPERATIONS AND METHODS - PART 2

#1. dict.key()
person = {'name': 'John', 'age': 35, 'location':'Soweto'}

k = person.keys()
print(k)
print(type(k)) # class 'dict_keys'

my_keys = list(k)
print(my_keys) # ['name', 'age', 'location']

#2. dict.value()
print(person.values())
print(list(person.values())) # ['John', 35, 'Soweto']

#3. dict.items()
print(person.items())

print('name' in person) # True
print(10 in person.keys()) # False
print(('age', 30) in person.items()) # False

d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values()
d1[10] = 'X'
print(v) # (['X', 'b', 'c'])

d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}
k1 = d1.keys()
k2 = d2.keys()
print(k1, k2) # dict_keys([10, 20]) dict_keys([20, 30])

for k in person.keys():
    print(f'key is {k}')

for v in person.values():
    print(f'value is {v}')

for k in person.keys():
    print(f'key is {k} and value is {person[k]}')

for k,v in person.items():
    print(f'key is {k} and value is {v}')