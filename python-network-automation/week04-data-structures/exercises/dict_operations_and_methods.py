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
# DICTIONARY OPERATIONS AND METHODS - PART 1
