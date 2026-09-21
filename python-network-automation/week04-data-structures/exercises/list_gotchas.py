print('#' * 10 + ' LIST GOTCHAS ' + '#' * 10)

# 1.
l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(10)
print(f'l2: {l2}')
print(f'l1: {l1}')
print(id(l1), id(l2))
l1.remove(2)
print(f'l2: {l2}')

l3 = l1.copy()
l3.append('abc')
print(f'l1: {l1}')
print(f'l3: {l3}')
print(id(l1), id(l3))

# 2.
nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2]

# THIS IS WRONG!!
# for n in nums:
#     if n < 5:
#         nums.remove(n)
# print(f'nums: {nums}') # [4, 5, 6, 7, 1, 2]

# THIS IS CORRECT!!
new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(f'new_list: {new_list}') # [5, 6, 7]

my_list = [n for n in nums if n >= 5]
print(f'my_list: {my_list}') # [5, 6, 7]
