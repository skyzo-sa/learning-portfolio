# Creates and manages the SSH connection .
from netmiko import ConnectHandler

# Handles common connection and authentication errors gracefully.
from netmiko.exceptions import (NetmikoTimeoutException,NetmikoAuthenticationException)
# DEVICE CONNECTION SETTINGS

# Store the Cisco router connection details in a dictionary.
cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.51",
    "username": "admin",
    "password": "P@ssw0rd",
    "secret": "P@ssw0rd",
    "port": 22,
}
# CONNECT TO THE ROUTER
try:
    print("Connecting to R3...")
# Automatically closes the connection when the work inside this block is complete.
    with ConnectHandler(**cisco_device) as connection:
        print("Connected successfully!") # Confirm that the SSH connection was successful.

# ENTER ENABLE MODE
        print("Entering enable mode...")
        connection.enable()

# RETRIEVE THE RUNNING CONFIGURATION
        print("Getting running configuration...")
        output = connection.send_command(
            "show running-config",
            read_timeout=60
        )
# FIND THE ROUTER HOSTNAME
        prompt = connection.find_prompt()
        hostname = prompt[0:-1]
        print("Hostname: ", hostname)

# CREATE THE BACKUP FILENAME
        filename = f"{hostname}-backup.txt"

# SAVE THE CONFIGURATION TO A FILE
        with open(filename, "w") as backup: # Open the backup file in write mode ("w").
            backup.write(output) # Write the running configuration collected

            # Confirm that the backup was successfully saved.
            print(f"Backup of {hostname} completed successfully!")
            # Print a separator for cleaner console output.
            print('#' * 30)

# DISPLAY THE RUNNING CONFIGURATION
        print(output)

# ERROR HANDLING

# error occurs when Netmiko cannot establish a TCP/SSH
except NetmikoTimeoutException:
    print("ERROR: Cannot reach R3 on TCP port 22.")

# router is reachable, but the supplied username or password is incorrect
except NetmikoAuthenticationException:
    print("ERROR: Authentication failed. Check username or password.")

# any other unexpected errors and display the error message.
except Exception as error:
    print(f"Unexpected error: {error}")