print('#' * 10 + ' Positional and Keyword Arguments ' + '#' * 10)
"""
A function can take parameters
that are a special kind of variable
used in a function as input.
"""
# FUNCTION POSITIONAL AND KEYWORD ARGUMENTS


#1. Positional arguments
def difference(a, b):
    result = a - b
    print(result)

# difference() # TypeError: missing 2 required positional arguments: 'a' and 'b'
difference(1, 5) # -4
"""
parameters vs. arguments
"""
def func1(x, y): # parameters
    print(f'1st parameter x is {x}') # 1st parameter x is Python
    print(f'2nd parameter y is {y}') # 2nd parameter y is 55

func1('Python', 55)  # arguments

#2. Keyword/Named arguments
def func2(x, y, z): # parameters
    print(f'1st parameter x is {x}') # 1st parameter x is 3
    print(f'2nd parameter y is {y}') # 2nd parameter y is 7
    print(f'3rd parameter z is {z}') # 3rd parameter z is 9

func2(y=7, x=3, z=9)
func2(10, 20, 30)

print('#' * 10 + ' FUNCTION DEFAULT ARGUMENTS ' + '#' * 10)

#3. Default arguments
def add(x, y=10):
    print(f'x is {x} and y is {y}') # x is 2 and y is 3
    print(f'{x} + {y} = {x + y}')

add(2, 3) # 2 + 3 = 5
add(6) # 6 + 10 = 16



