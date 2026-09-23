print('#' * 10 + ' For, continue and pass statements ' + '#' * 10)
# For, continue and pass statements

for letter in 'Go Python goooo!':
    if letter == 'o':
        continue
    print(letter, end='')

for n in range(10):
    if n % 2 == 0:
        print(f'FOund an even number: {n}')
        continue
    print(f'Found an odd number: {n}')


for _ in range(100):
    pass
