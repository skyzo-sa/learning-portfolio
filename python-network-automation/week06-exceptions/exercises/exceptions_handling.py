print('#' * 10 + ' EXCEPTIONS HANDLING ' + '#' * 10)
#  EXCEPTIONS HANDLING

while True:
    try:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        d = 7
        c = a / b + d
        print(c)

    except ZeroDivisionError as e:
        print(f'Division by zero is not permitted: {e.args}.')

    except TypeError as e:
        print(f'Operations of different types are not permitted: {e}.')

    except Exception as e:
        print(f'A generic exception has occurred: {e.args}.')
    else:
        print('No errors!')
        print(f'c = {c}')
        break

    finally:
        print('#' * 10)
        print('#' * 10 + ' GOOD BYE! ' + '#' * 10)

x = 10
print(x**x)
print('#' * 10)
print('Some other code...')

age = -1
if age < 0:
    raise Exception('Age below zero is not permitted!')