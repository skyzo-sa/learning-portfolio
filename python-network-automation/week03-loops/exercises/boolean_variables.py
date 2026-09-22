print('#' * 10 + ' BOOLEAN VARIABLES ' + '#' * 10)
# BOOLEAN VARIABLES
"""
BOOLEAN VARIABLES AND EXPRESSIONS
A boolean variable is an object of the bool() class
which is an int() subclass.

Boolean constants:
1. True
2. False
"""
print('#' * 10 + ' STATEMENTS VS. EXPRESSIONS ' + '#' * 10)

"""
STATEMENTS VS. EXPRESSIONS
A statement is a unit of code and an expression is a 
special statement that can be evaluated to some value.
"""

# TRUTHINESS OF OBJECTS

result = ''
if bool(result):
    print('result is not empty.')
else:
    print('result is empty.')
