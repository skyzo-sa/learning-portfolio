from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# List of Cisco routers to back up

cisco_devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.51",
        "username": "admin",
        "password": "P@ssw0rd",
        "secret": "P@ssw0rd",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.23",
        "username": "admin",
        "password": "P@ssw0rd",
        "secret": "P@ssw0rd",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.52",
        "username": "admin",
        "password": "P@ssw0rd",
        "secret": "P@ssw0rd",
        "port": 22,
    }
]

# Loop through each router

for cisco_device in cisco_devices:

    try:
        print(f"\nConnecting to {cisco_device['host']}...")

        with ConnectHandler(**cisco_device) as connection:

            print("Connected successfully!")

            print("Entering enable mode...")
            connection.enable()

            print("Getting running configuration...")
            output = connection.send_command(
                "show running-config",
                read_timeout=60
            )

            # Get the hostname from the router prompt
            prompt = connection.find_prompt()
            hostname = prompt[0:-1]

            print("Hostname:", hostname)

            # Create a backup file using the hostname
            filename = f"{hostname}-backup.txt"

            with open(filename, "w") as backup:
                backup.write(output)

            print(f"Backup of {hostname} completed successfully!")
            print("#" * 30)

            # DISPLAY THE RUNNING CONFIGURATION
            print(output)

    except NetmikoTimeoutException:
        print(f"ERROR: Cannot reach {cisco_device['host']} on TCP port 22.")

    except NetmikoAuthenticationException:
        print(f"ERROR: Authentication failed for {cisco_device['host']}.")

    except Exception as error:
        print(f"Unexpected error: {error}")

print("\nAll router backup attempts completed.")