# GETTING USER INPUT
print('#' * 10 + 'GETTING USER INPUT' + '#' * 10)


# name = input('Enter your name:')
# print('Your name is ', name)
# # class 'str'
# print(type(name))

price = input('Enter price:')
quantity = input('Enter quantity:')
# TypeError: can't multiply sequence by non-int
# total_value = price * quantity

total_value = float(price) * float(quantity)
# total_value = int(price) * int(quantity)
print(total_value)
