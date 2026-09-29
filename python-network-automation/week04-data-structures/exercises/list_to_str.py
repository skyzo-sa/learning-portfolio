print('#' * 10 + ' LIST TO STRING ' + '#' * 10)
# split() and join()

s1 = 'I am learning Python Programming!'
l1 = s1.split()
print(l1) # ['I', 'am', 'learning', 'Python', 'Programming!']

ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
ip_str = ' , '.join(ip_list)
print(ip_str) # 192.168.0.1 , 192.168.0.2 , 192.168.0.3
