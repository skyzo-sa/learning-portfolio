print('#' * 10 + 'OPERATORS' + '#' * 10)

"""
An operator is a symbol of the
programming language able to operate on values.
"""

# Order of operations (operator precedence)
"""
1. Exponentiation (**)
2. Multiplication (*)
3. Division (//)
4. Addition (+)
5. Subtraction (-)
"""
print(2 + 4 * 2 ** 3) # Answer is: 34
print((2 + 4) * 2 ** 3) # Answer is: 48

"""
Arithmetic Operators:
"""

# (+) addition
print(5 + 5)

# (-) minus
print(3 - 9)

# (/) division - returns a float 2.0
print (8 / 4)

# (//) floor division
print(11 // 2)

# (*) multiplication
print(5 * 4)

# (**) exponentiation, raising to a power
print(2 ** 100)

# (%) modulus (mod), returns remainder of division of left operant
print(8 % 5) # 5 goes 1 times in 8 and remainder is 3
print(14 % 4) # 4 goes 3 times in 14 and remainder is 2

print (5 * 5.0) # returns a float 25.0

print(1_000_000_000) # Ignores the underscores returns 1000000000
print(1000 == 1_000) # True