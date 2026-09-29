print('#' * 10 + ' TUPLE OPERATIONS ' + '#' * 10)
# TUPLE OPERATIONS

my_tuple = (1.4, 10, 'abcd', True, (30, 40), 'x')
t1 = my_tuple + tuple('yz')
print(t1)

t2 = (1, 2, 'a') * 3
print(t2)
print(my_tuple[0:2])
print(my_tuple[:3])
print(my_tuple[2:])
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[-1:0:-1])

movies = ('The Wizard of Oz', 'The Legend', 'Casablanca')
for movie in movies:
    print(f'We are watching {movie}')

print('The Legend' in movies) # True
print('The Legend' not in movies) # False