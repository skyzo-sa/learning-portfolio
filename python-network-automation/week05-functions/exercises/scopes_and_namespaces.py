print('#' * 10 + ' SCOPES AND NAMESPACES ' + '#' * 10)
# SCOPES AND NAMESPACES

"""
A namespace is a container(table) that contains the names we define.
This way we can have the same name defined in different namespaces.

The portion of code where the name exists is called: scope of that
name and the binding between the name and the value is stored in a namespace.
"""
t1 = tuple(range(10))
print(t1)
#1. The Built-in Namespace: Python built-in functions.

#2. The Global(Module Namespace): names defined in scripts.

#3. The Local Namespace: names defined inside functions.


x = 10

def my_func():
    global x
    x += 1
    print(f'x inside the function: {x}')

my_func() # x inside the function: 11

print(len('abc'))
def len(x):
    print(x)
del len
print(len('abcdefgh'))

numbers = [1, 2, 3]
x = 10

def my_function(numbers, x):
    numbers.append(5)
    x = 66
    print(f'x inside the function: {x}')

my_function(numbers, x) # x inside the function: 66
print(f'After calling the function, number is {numbers} and x is {x}') # [1, 2, 3, 5] and x is 10