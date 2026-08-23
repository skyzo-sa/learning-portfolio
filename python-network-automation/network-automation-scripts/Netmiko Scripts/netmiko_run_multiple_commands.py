from netmiko import ConnectHandler

cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.23',
        'username': 'admin',
        'password': 'P@ssw0rd',
        'port': 22,
        'secret': 'P@ssw0rd',
        'verbose':True
        }

connection = ConnectHandler(**cisco_device)

connection.enable()

commands = ['int loopback 0', 'ip address 7.7.7.7 255.255.255.255', 'exit', 'username admin2 secret cisco']
output = connection.send_config_set(commands)
print(output)


output = connection.send_command_expect('write memory')
print(output)

connection.disconnect()