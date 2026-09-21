print('#' * 10 + 'ASSIGNMENT OPERATORS' + '#' * 10)

"""
Assignment Operators:
"""

# (=) Equals
a = 5

# (=+) Plus equals
a += 2 # shorthand for a = a + 2 => a is 7
print(a)

# (-=) Minus equals
a -= 3 # shorthand for a = a - 3 => a is 4
print(a)

# (*=) Star equals
a *= 3 # shorthand for a = a * 3 => a is 12
print (a)

# (/=) Slash equals
a /= 2 # shorthand for a / 2 => a is 6
print(a)

# (**=) Double stars equals
a **= 2 # shorthand for a = a ** 2 => a is 36
print(a)

# (%=) Percent equals


"""
Built-in Functions
"""
# divmod()
a, b = divmod(14, 6) # 2 2
print(a, b)

# pow()
print(pow(5, 9)) # 1953125

# sum()
print(sum([1, 2, 5, 6, 7, 7, 9])) # 37

# max()
print(max([1, 2, 5, 6, 7, 7, 9])) # 9

# min()
print(min([1, 2, 5, 6, 7, 7, 9, -6])) # -6

# round()
a = 5.666772
print(round(a, 3)) # 5.667