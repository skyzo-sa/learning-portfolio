print('#' * 10 + ' VARIABLE-LENGTH ARGUMENTS: *args ' + '#' * 10)
# VARIABLE-LENGTH ARGUMENTS: *args

#1. *args
def average(a, b, *args):
    # print(f'args is: {args}')
    # return (a + b) / 2
    return (a + b + sum(args)) / (2 + len(args))

def concatenate(*args):
    result = ''
    for tmp in args:
        result = result + tmp
    return result

# print(average(4, 5, 6, 7)) # 4.5
r = concatenate('Python', '3', '!')
print(r)  # Python3!


print('#' * 10 + ' VARIABLE-LENGTH ARGUMENTS ' + '#' * 10)
# VARIABLE-LENGTH ARGUMENTS: **kwargs

#2. **kwargs
def my_function(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'k is: {k}, v is: {v}')

my_function(name = 'John Wick') # k is: name, v is: John Wick

person = {'name':'Ernest', 'age':35, 'location': 'Johannesburg'}
my_function(**person)

def connect(ip, port, username, password):
    print(ip, port, username, password)

linux_server = {'ipaddress':'172.168.10.1', 'port':22, 'username':'admin', 'password':'P@ssw0rd2026!'}
connect(**linux_server)
