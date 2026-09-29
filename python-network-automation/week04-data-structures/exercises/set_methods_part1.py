print('#' * 10 + ' SETS METHODS - PAR 1 ' + '#' * 10)
# PYTHON SETS METHODS - PAR 1

#1. set.add(item)
s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)

s1.add(1) # it does nothing!
# print(s1)

#2. set.remove(item)
s1.remove(3) # {1, 2, 4.5, 'a'}
print(s1)
# s1.remove(3)  # KeyError: 3

#3. set.discard(item)
s1.discard('a') # {1, 2, 4.5}
print(s1)
s1.discard('x') # No error

#4. set.pop()
x = s1.pop()
print(x, s1)

s2 = set('abc')
s3 = s2
s3.add('x') # {'c', 'b', 'a', 'x'}
print(s2)


#5. set.clear()
s3.clear()
print(f's2: {s2}', f's3: {s3}')

#6. set.copy()
s4 = s1.copy()
s4.add('z')
print(f's4: {s4}', f's3: {s1}') # s4: {'z', 2, 4.5} s3: {2, 4.5}






