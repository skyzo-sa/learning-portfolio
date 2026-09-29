from netmiko import ConnectHandler

cisco_device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.10",
    "username": "u1",
    "password": "cisco",
    "secret": "cisco",
}

vlans = {
    100: ["GigabitEthernet1/0/10", "GigabitEthernet1/0/11"],
    200: ["GigabitEthernet1/0/20", "GigabitEthernet1/0/21"],
    300: ["GigabitEthernet1/0/30"]
}

conn = ConnectHandler(**cisco_device)
conn.enable()

for vlan, interfaces in vlans.items():
    commands = [f"vlan {vlan}"]

    for intf in interfaces:
        commands.extend([
            f"interface {intf}",
            "switchport mode access",
            f"switchport access vlan {vlan}",
            "no shutdown"
        ])

    output = conn.send_config_set(commands)

    print(f"\n=== VLAN {vlan} Configuration ===")
    print(output)

conn.disconnect()