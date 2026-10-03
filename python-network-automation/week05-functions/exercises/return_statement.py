print('#' * 10 + ' THE RETURN STATEMENT ' + '#' * 10)
# THE RETURN STATEMENT

n = len([1, 2, 4, 5])
print(n)

def add1(a, b):
    print(f'Sum: {a + b}')

def add2(a, b):
    return a + b
    print('XXXXXXXXXX')
    x = 10
    print(x * 2)

def func1():
    pass

add1(10, 20)
my_sum = add2(5, 2) # Sum: 30
print(my_sum) # 7

def my_func(x):
    return x, x**2, x**3, x**4

print(my_func(3)) # (3, 9, 27, 81)
a, b, c, d = my_func(10)
print(a, b, c, d) # 10 100 1000 10000