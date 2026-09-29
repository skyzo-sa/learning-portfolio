from netmiko import ConnectHandler

# Device details
cisco_device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.10",
    "username": "u1",
    "password": "cisco",
    "port": 22,
    "secret": "cisco",
    "verbose": True,
}

# Connect to the switch
connection = ConnectHandler(**cisco_device)

# Enter enable mode
connection.enable()

# VLAN and interface configuration
vlan_id = 100
vlan_name = "USERS"
interface = "GigabitEthernet1/0/10"

commands = [
    f"vlan {vlan_id}",
    f"name {vlan_name}",
    f"interface {interface}",
    "switchport mode access",
    f"switchport access vlan {vlan_id}",
    "no shutdown"
]

# Send configuration commands
output = connection.send_config_set(commands)

print("\n===== Configuration Output =====")
print(output)

# Verify VLAN
print("\n===== VLAN Verification =====")
print(connection.send_command(f"show vlan id {vlan_id}"))

# Verify Interface
print("\n===== Interface Verification =====")
print(connection.send_command(f"show interfaces status | include {interface}"))

# Disconnect
connection.disconnect()