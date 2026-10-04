print('#' * 10 + ' PROJECT: TEST NETWORK CONNECTIONS ' + '#' * 10)
# PROJECT: TEST NETWORK CONNECTIONS
import subprocess
with open('hosts.txt') as file:
    ip_addresses = file.read().splitlines()
    # print(ip_addresses)
    for ip in ip_addresses:
        try:
            command = f'ping -n 4 {ip}'
            # command = 'ping -c 4 8.8.8.8' # Linux / Mac
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'Host {ip} is down!!! => {e}')
        print('#' * 50)