print('#' * 10 + ' PYTHON SETS ' + '#' * 10)
# PYTHON SETS
"""
Mutable unordered collections of unique elements.
"""
s1 = {1, 2, 3, 'a', 'b', 4, 1, 2, 'a', 3, 10}
print(s1)

# print (s1[0]) # TypeError: 'set' object is not subscriptable

# SETS ARE MUTABLE
s1.add((10, 20))
print(s1)

s1.remove('a') # 1, 2, 3, 4, 10, 'a', 'b', (10, 20)
print(s1) # 1, 2, 3, 4, 10, 'b', (10, 20)

# l1 = [1, 2]
# s1.add(l1)
# print(s1) #TypeError: cannot use 'list' as a set element

s2 = set()
s3 = {} # class 'dict'
print(type(s3))

# str => set
s4 = set('Helloooooo') # {'l', 'H', 'o', 'e'}
print(s4)

# tuple => set
s5 = set((1, 2, 3, 4, 4, 'abc')) # {1, 2, 3, 4, 'abc'}
print(s5)

# list => set
l2 = [10, 20, 30, 40, 50] # {40, 10, 50, 20, 30}
print(set(l2))

mac_address = ['AC-91-A1-54-B7-FC', ' AC-91-A1-54-B7-FC', ' AC-91-A1-54-B7-FC',
               'AC-91-A1-54-B7-FC', ' AC-91-A1-54-B7-FC', ' AC-92-A1-54-B7-F8']
macs = set(mac_address)
print(macs)
print(len(macs)) # 3

for item in s4:
    print(item)

set1 = {1, 2, 3}
set2 = {2, 3, 1}

print(set1 == set2) # True
print(set1 is set2) # False
print([1, 2, 3] == [2, 3, 1]) # False