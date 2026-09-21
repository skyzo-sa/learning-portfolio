# STRING METHOD
print('#' * 10 + 'string_method' + '#' * 10)


# print(), len(), type(), sum(), max(), min(), round()
# print(len('xfdsa'))
#
# print(dir(str))
# help(str.replace)
#
# s = 'Python'
# new_s = s.upper()
# print(s)
# print(new_s)
#
# print('prOgrammIng'.lower())


my_str = 'I learn Python Programming.'

#1.str.upper()
print(my_str.upper())

#2.str.lower()
print(my_str.lower())

#3.str.strip()
ip = '192.168.18.1    '
ip = ip.strip()
print(ip)

value = '$$300$$$$'
print(value.strip('$'))

#4.str.replace()
new_value = value.replace('$', 'R')
print(new_value)

#5.str.count()
txt = 'I learn Python, Python is cool!'
n = txt.count('Python')
print(n)

#6.str.split()
my_list = txt.split()
print(my_list)

#7.str.join()
ip =  '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list)
print(ip_str)

#7.str.find()
my_str = 'I learn Python Programming.'
print(my_str.find('Python'))

# in
print('Python' in my_str)

# not in
print('Golang' not in my_str)