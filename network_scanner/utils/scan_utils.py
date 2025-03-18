import platform
import subprocess
import re
from ..utils import RED, GREEN, CYAN, RESET

def ping(ip):
    """Ping an IP address to check if it's live."""
    try:
        cmd = ["ping", "-c", "1", "-W", "0.5", ip] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "500", ip]
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"{GREEN}[LIVE] {ip}{RESET}")
            return ip
    except Exception as e:
        print(f"{RED}Error pinging {ip}: {e}{RESET}")
    return None

def arp_scan():
    """Retrieve all IP and MAC addresses of connected devices using ARP."""
    print("\n[INFO] Running ARP scan to detect all connected devices...\n")
    devices = []
    try:
        if platform.system() == "Windows":
            cmd = ["arp", "-a"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]+)", result.stdout)
        else:
            cmd = ["ip", "neigh"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+.*\s+([a-fA-F0-9:-]+)", result.stdout)

        if pattern:
            print("Connected Devices:")
            print("-----------------------------------------")
            print(f"{CYAN}IP Address\t\tMAC Address{RESET}")
            print("-----------------------------------------")
            for ip, mac in pattern:
                devices.append((ip, mac))
                print(f"{GREEN}{ip}\t{mac}{RESET}")

    except Exception as e:
        print(f"{RED}Error performing ARP scan: {e}{RESET}")
    
    return devices
