print('#' * 10 + ' WHILE AND BREAK ' + '#' * 10)
"""
The break statement breaks out of the innermost
enclosing for or while loop.

If the break statement is inside a nested loop,
break will terminate only the innermost loop.
"""
# WHILE AND BREAK
while True:
    guess = int(input('Enter your lucky number [1-10]:'))
    if guess == 7:
        print('You win!')
        break
    print(f'{guess} was not a lucky number! ')

a = int(input('Enter a number: '))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            break
        b -= 1
    else: # belongs to the inner while
        print(f'{a} is prime! ')
    a -= 1
    

