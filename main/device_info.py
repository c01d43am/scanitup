import subprocess
import re
from network_utils import GREEN, CYAN, RED, RESET

def arp_scan():
    """Retrieve all IP and MAC addresses of connected devices using arp-scan."""
    devices = []
    try:
        cmd = ["sudo", "arp-scan", "-l"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]+)\s+(.+)", result.stdout)
        
        if pattern:
            print(f"\n{CYAN}Connected Devices:{RESET}")
            print("-----------------------------------------")
            print(f"{CYAN}IP Address\tMAC Address\tDevice Name{RESET}")
            print("-----------------------------------------")
            for ip, mac, name in pattern:
                devices.append({"ip": ip, "mac": mac, "name": name})
                print(f"{GREEN}{ip}\t{mac}\t{name}{RESET}")

    except Exception as e:
        print(f"{RED}Error performing ARP scan: {e}{RESET}")
    
    return devices
