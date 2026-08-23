from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'ip': '192.168.1.3',
    'username': 'root',
    'password': 'eve',
    'port': 22,
    'session_log': 'netmiko_linux.log',
    'verbose': True
}

connection = ConnectHandler(**linux)

output = connection.send_command_timing(
    'apt update && apt upgrade -y',
    last_read=10,
    read_timeout=300
)

print(output)

connection.disconnect()