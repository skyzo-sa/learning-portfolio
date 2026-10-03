print('#' * 10 + ' LAMBDA EXPRESSIONS ' + '#' * 10)
# LAMBDA EXPRESSIONS
"""
Another way of creating functions.

They're called anonymous functions because they don't have a name
(they are a single line of logical code.)

The terms lambda expressions, lambda functions, anonymous functions,
or function literals can be used interchangeably.
"""

# SYNTAX - lambda parameter_list: expression

def add(a, b, c):
    result = a + b + c
    return result

result = (lambda a, b, c: a + b + c)(3, 4 , 5)
print(result)

square =  lambda x: x ** 2
print(square(4))

