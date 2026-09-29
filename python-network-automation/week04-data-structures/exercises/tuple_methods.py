print('#' * 10 + ' TUPLE METHODS ' + '#' * 10)
"""
tuple.index() and tuple.cound()
"""
# TUPLE METHODS

t1 = (1, 2, 1, 3, 4)

#1. tuple.index()
i = t1.index(2)
print(f'2 is at position {i}') # 2 is at position 1

# i = t1.index(x) # NameError: name 'x' is not defined
x = 10
if x in t1:
    i = t1.index(x)
    print(f'x is at position {i}')
else:
    print(f'{x} is not in tuple')

#2. tuple.count()
n = t1.count(1)
print(n) # => 2

# TEST MEMBERSHIP
print(100 in t1) # False

# len(), sum(), max(), min(), sorted()
print(len(t1)) # => 5
print(sum(t1)) # => 11
print(max(t1)) # => 4
print(min(t1)) # => 1

t2 = sorted(t1)
print(t2) # [1, 1, 2, 3, 4]

t2 = sorted(t1, reverse=True)
print(t2) # [4, 3, 2, 1, 1]