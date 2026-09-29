import os
import platform
import subprocess
import re

def get_default_gateway():
    system = platform.system()

    if system == "Windows":
        output = subprocess.check_output("ipconfig", shell=True).decode()
        match = re.search(r"Default Gateway . . . . . . . . . : (\S+)", output)
    else:
        output = subprocess.check_output("ip route", shell=True).decode()
        match = re.search(r"default via (\S+)", output)

    if match:
        return match.group(1)
    return None


def ping_host(host):
    print(f"\n🔎 Pinging {host}...")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    subprocess.call(["ping", param, "4", host])


def check_speed():
    print("\n🚀 Checking Internet Speed...")
    subprocess.call(["speedtest-cli"])


def traceroute(host):
    print(f"\n🛰️ Tracing route to {host}...")
    cmd = "tracert" if platform.system().lower() == "windows" else "traceroute"
    subprocess.call([cmd, host])


def main():
    print("====== NETWORK HEALTH CHECK ======")

    gateway = get_default_gateway()

    if gateway:
        print(f"Default Gateway: {gateway}")
        ping_host(gateway)
    else:
        print("Could not detect default gateway.")

    check_speed()
    traceroute("8.8.8.8")


if __name__ == "__main__":
    main()