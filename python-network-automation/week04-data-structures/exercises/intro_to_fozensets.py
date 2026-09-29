print('#' * 10 + ' PYTHON FOZENSETS ' + '#' * 10)
# PYTHON FROZENSETS
"""
Immutable unordered collections of unique elements.
"""

fs1 = frozenset({1, 2, 3, 'a', 'b', 'c'})
print(fs1, type(fs1)) # class 'frozenset'

s1 = 'Python is cool!!'
fs2 = frozenset(s1)
print(fs2, type(fs2))

fs1 =  frozenset([1, 2, 3, 4, ])
fs2 = frozenset([3, 4, 5, 6])
fs3 = fs1.intersection(fs2)
print(fs3, type(fs3))  # ({3, 4})

s1 = {4, 10, 20}
result1 = s1.intersection(fs1) # set
result2 = fs1 - s1 # frozenset

print(f'result1 = {result1}', type(result1)) # 'set'
print(f'result2 = {result2}', type(result2)) # 'frozenset'