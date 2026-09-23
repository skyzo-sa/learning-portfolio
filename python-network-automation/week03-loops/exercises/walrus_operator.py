print('#' * 10 + ' WALRUS OPERATOR ' + '#' * 10)
# WALRUS OPERATOR
'''
SYNTAX OF OPERATOR: name := expression
'''
print(x := 2 + 3)
print(f'x is: {x}')

# Method 1

# value = input('Enter a something: ')
# while value != '':
#     print(f'You entered: {value}')
#     value = input('Enter a something: ')

# Method 2
while (value := input('Enter a something: ')) != '':
    print(f'You entered: {value}')

data = input('Enter your name: ')
if (n := len(data)) > 0:
    print(f'Your name has {n} characters.')
else:
    print('Your name cannot be empty.')