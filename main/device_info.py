import platform
import subprocess
import re

def arp_scan():
    """Retrieve all IP and MAC addresses of connected devices using ARP."""
    devices = []
    try:
        if platform.system() == "Windows":
            cmd = ["arp", "-a"]
        else:
            cmd = ["ip", "neigh"]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+.*\s+([a-fA-F0-9:-]+)", result.stdout)

        for ip, mac in pattern:
            devices.append({"ip": ip, "mac": mac})
    
    except Exception as e:
        print(f"Error performing ARP scan: {e}")
    
    return devices
