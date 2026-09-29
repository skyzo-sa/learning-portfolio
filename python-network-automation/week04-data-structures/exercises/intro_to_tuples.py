print('#' * 10 + ' TUPLES ' + '#' * 10)
"""
TUPLES ARE IMMUTABLE (can't be changed).
"""
# PYTHON TUPLES

t1 = tuple()
t2 = ()
print(type(t1), type(t2)) # class 'tuple'> <class 'tuple'

t3 = (1, 3.4, 'python', True)
print(t3) # (1, 3.4, 'python', True)

t4 = (10)
print(type(t4)) # class 'int'

t4 = (10,)
print(type(t4)) # class 'tuple'

t5 = 6.9, True, 10, 'abc'
print(type(t5)) # class 'tuple'

t6 = tuple([1, 2, 3, 4])
t7 = tuple('Hello Python')
print(type(t6), type(t7)) # class 'tuple'> <class 'tuple'

l1 = list(t5)
print(l1) # [6.9, True, 10, 'abc']

print(t5[0]) # 6.9
print(t5[-1]) # abc