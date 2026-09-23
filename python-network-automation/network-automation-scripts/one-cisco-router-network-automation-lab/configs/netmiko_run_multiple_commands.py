from netmiko import ConnectHandler

# Define the dictionary containing device connection parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.23',
    'username': 'admin',
    'password': 'P@ssw0rd',
    'port': 22,
    'secret': 'P@ssw0rd',
    'verbose': True
}

# Establish the SSH connection
connection = ConnectHandler(**cisco_device)

# Enter privileged EXEC mode
connection.enable()

# Define the list of configuration commands to send
commands = [
    'int loopback 0',
    'ip address 7.7.7.7 255.255.255.255',
    'exit',
    'username admin2 secret cisco'
]

# Send the configuration commands and print the terminal output
output = connection.send_config_set(commands)
print(output)

# Save the running configuration and print the output
output = connection.send_command_expect('write memory')
print(output)

# Disconnect the SSH session safely
connection.disconnect()