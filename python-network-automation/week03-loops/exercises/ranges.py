print('#' * 10 + ' RANGES ' + '#' * 10)
# RANGES

r = range(2, 10)
print (type(r))
print(list(r))

print (list(range(0, 11, 2)))
print(list(range(0, 40, 78)))
s = sum(range(0, 1001))
print(s)

# Summary
# 1. range(stop)
print(list(range(10))) # range(0, 10, 1)

# 2. range(start, stop)
print(list(range(3, 9))) # range(3, 9, 1)

# 3. range(start, stop, step)
print(list(range(5, 100, 13))) # range(3, 9, 1)
