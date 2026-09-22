print('#' * 10 + ' LOOPS AND RANGES ' + '#' * 10)

# LOOPS AND RANGES

s = 0
for n in range(101): # range(0, 101, 1)
    s += n
print(f'Sum: {s}')

for n in range(10):
    print('Do Something')

import  random
names = ['Diana', 'Paul', 'Ana', 'Dan', 'Victor', 'Marry', 'Maria', 'Mathew', 'Kevin']
for _ in range(3):
    print(f'Choosing winner. Round {_}...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('########')
