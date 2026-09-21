# PYTHON LISTS
print('#' * 10 + ' INTRO TO LISTS ' + '#' * 10)


l1 = [1, 2,5, 'python', True, ['abc', 'xyz'], (10, 20, 30)]
print(len(l1))
l2 = [] # empty list
l3 = list() # empty list

print(l1[0])
x = l1[-1]
print(x)

#TypeError:
# s1 = 'abc'
# s1[0] = 'X' # str is immutable
# print(s1)

l4 = list('abcd')
print(l4)
print(id(l4))
l4[0] = 'X'
l4.append(100)
print(l4) # ['X', 'b', 'c', 'd', 100]
