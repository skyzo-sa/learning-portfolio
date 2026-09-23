print('#' * 10 + ' For, else and break statements ' + '#' * 10)
# For, else and break statements

for number in range(10):
    print(number)
    if number == 5:
        break
# exit() - stops the entire script.
print('Outside for')

for letter in 'Python':
    if letter == 'o':
        print('letter is o and I\'m breaking out of the loop ...')
        break
    print(letter)


for n in range(0, 20):
    if n % 13 == 0:
        print('There is a number divisible by 13 in the range. Breaking out ...')
        break
else: # belongs to for
    print ('THere is no number divisible by 13 in the range.')


for l in 'abc':
    print(l)
    for n in range(3):
        if n == 1:
            break