print('#' * 10 + ' DICTIONARIES ' + '#' * 10)
# PYTHON DICTIONARIES
"""
An ordered collection of keys:value pairs,
separated by commas, and enclosed by curly braces.{}
"""
person = {"name": "John", "age": 25, "city": "New York", 10:('a', 'b')}
print(type(person)) # dict
d1 = dict()
print(type(d1)) # dict


print('#' * 10 + ' WORKING WITH DICTIONARIES ' + '#' * 10)
# WORKING WITH DICTIONARIES
print(len(person)) # 4

person['name'] = 'John Wick'
print(person)

person['age'] = 30
print(person)

person['city'] = 'Katlehong'
print(person) # {'name': 'John Wick', 'age': 30, 'city': 'Katlehong', 10: ('a', 'b')}

a = person['age']
print(a)

value = person.get('name', 'Unknown, key does not exist')
print(value)

name = person.pop('name')
print(name, person)

print(person.popitem())

del person['age']
print(person) # {'city': 'Katlehong'}

germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
}
print(germany['cities'][1]) # Berlin
print(germany['info']['people'][-1]) # Gauss

countries = [
    {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
    },
    {
        'cities': ['Paris', 'Lyon', 'Bordeaux'],
        'info': {'population': 67_000_000, 'person': ['Monet', 'Marie Curie', 'Napoleon']}
    }
]
print(countries[0]['cities']) # ['Hamburg', 'Berlin', 'Munich']
print(countries[1]['info']['person'][1]) # 'Marie Curie'