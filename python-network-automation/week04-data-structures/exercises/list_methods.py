# LIST METHODS
"""
Extend(), Inset(), Copy(), Clear(), Pop(), Remove()
"""
print('#' * 10 + ' LIST METHODS ' + '#' * 10)

l1 = list()
print(dir(l1)) # ['__add__', '__class__', '__class_getitem__', '__contains__']
help(l1.append) # method of builtins.list instance

# Adding to the list: append(), extend(), insert()
l1 = [1, 2.2, 'abc']

# 1. list.append()
l1.append(5)
# l1.append(6, 7) # TypeError: list.append() takes exactly one argument (2 given)
# l1.append(6, 7)
# print(l1)

# 2. list.extend()
l1.extend(['x', 'y'])
print(l1) # [1, 2.2, 'abc', 5, 'x', 'y']

# 3. list.insert()
years = [2020, 2022, 2023]
years.insert(1, 2021)
years.insert(len(years), 2024)
print(years)
years.insert(-1, 2025) # inserts on the second to last position.
print(years)

# 4. list.clear()
years.clear()
print(years)

# 5. list.pop()
l2 = [10, 20, 30, 40, 50]
x = l2.pop()
print(x)
print(l2)

y = l2.pop(1) # => 20
print(y, l2)

# l2.pop(100) #IndexError: pop index out of range

# 6. list.remove()
l3 = [10, 20, 10, 40, 20, 10, 20, 20, 'z']
# l3.remove(x) # ValueError: list.remove(x): x not in list
l3.remove(10)
print(l3)   # [20, 10, 40, 20]

while 20 in l3:
    l3.remove(20)
print(l3)   # => [10, 40, 10, 'z']


# LIST METHODS - PART 2
print('#' * 10 + ' LIST METHODS - PART 2 ' + '#' * 10)

# 7. list.index()
names = ['John', 'Debby', 'Kevin', 'Leroy', 'Mathew']
i = names.index('Debby')
print(f'Debby is at index {i}') # Debby is at index 1

# 8. list.count()
letter = list('asasredgfsadfglkhnasdlkkfpaiuhflkamwef')
n = letter.count('a')
print(n) # 6 a's

print('q' in letter)  # False

# 9. list.reverse()
l1 = [1, 3, 'abc', 10, 'x']
l1.reverse()
print(f'l1: {l1}') # ['x', 10, 'abc', 3, 1]

# 10. list.sort() and sorted(list)
ages = [10, 8, 23, 40, 35]
la = sorted(ages)
print(la, ages)

n = ages.sort()
print(n) # None
print(ages) # [8, 10, 23, 35, 40]

ages.sort(reverse=True)
print(ages) # [40, 35, 23, 10, 8]

# l1 = [1, 3, '5']
# l1.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

# 11. max(), min() and sum()
l2 = [-9, 10, 5, 100, 66]
print(f'max: {max(l2)}') # 100
print(f'min: {min(l2)}') # -9
print(f'sum: {sum(l2)}') # 172

