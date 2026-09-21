# LIST CONCATENATION
print('#' * 10 + ' LIST CONCATENATION ' + '#' * 10)

l1 = [3, 4]
print(l1, id(l1))
l1 = l1 + [5, 6]
print(l1, id(l1))

l1 += [7, 8]
print(l1, id(l1))

l1.extend([11, 12])
print(l1, id(l1))

# append vs. extend
l1.append(['a', 'b'])
print(l1)
l1.extend(['x', 'y'])
print(l1)
l1.append([20])
l1.extend([20])
print(l1)
# l1.extend(20) # TypeError:

l2 = list('abc')
l3 = l2 * 3
print(l3)

# LIST SLICING AND ITERATION
print('#' * 10 + ' LIST SLICING ' + '#' * 10)

numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}') # [2, 3, 4]
print(f'numbers: {numbers}') # [1, 2, 3, 4, 5]

print(numbers[:3]) # start is default zero.
print(numbers[2:]) # sto is default the end of the list.
print(numbers[::]) # [1, 2, 3, 4, 5]
print(numbers[::-1]) # [5, 4, 3, 2, 1]

print('#' * 10 + ' LIST ITERATION ' + '#' * 10)

ip_list = ['192.168.18.1', '192.168.18.2', '10.0.0.1']
for ip in ip_list:
    print(f'Connecting to {ip}...')
print('10.0.0.1' in ip_list) # True
print('192.100.0.2' in ip_list) # False


