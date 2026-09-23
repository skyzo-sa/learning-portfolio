print('#' * 10 + ' for loops ' + '#' * 10)
# FOR LOOPS
"""
for and while
"""
for letter in 'Python':
    print(letter)

my_str = input('Enter something: ')
vowels = 'aeiou'
for item in my_str:
    if item in vowels:
        print(item, end='')
