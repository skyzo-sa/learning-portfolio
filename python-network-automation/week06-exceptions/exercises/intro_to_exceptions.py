print('#' * 10 + ' ERRORS AND EXCEPTIONS HANDLING ' + '#' * 10)
# PYTHON ERRORS AND EXCEPTIONS HANDLING
"""
1. SYNTAX (parsing) errors
2. Exceptions (run-time errors)
"""

d1 = {'a' : 4}
# print(d1['b']) # KeyError: 'b'

# for x in range(10)
#     print(x) # SyntaxError: expected ':'

# for x in range(10):
# print(x) # IndentationError:

# with open(hello.txt) as f: # NameError: name 'hello' is not defined.
#     print(f.read())

# with open('hella.txt') as f: # FileNotFoundError: [Errno 2]
#     print(f.read())

with open('hello.txt') as f:
    print(f.read())

a, b = 10, 0
# print(a/b) # ZeroDivisionError: division by zero

# print(a + '7') # TypeError: unsupported operand type(s) for +: 'int' and 'str'