import socket
import ipaddress
import subprocess
import platform
import re

# ANSI color codes
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"{CYAN}[INFO] Local IP Detected: {local_ip}{RESET}")
        return local_ip
    except Exception as e:
        print(f"{RED}Error getting local IP: {e}{RESET}")
        return None

def get_subnet_mask():
    """Retrieve the subnet mask correctly for Windows and Linux."""
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["netsh", "interface", "ip", "show", "address"], capture_output=True, text=True)
            match = re.search(r"Subnet Prefix.*?:\s+([\d\.]+)", result.stdout)
            if match:
                return match.group(1)
        else:
            result = subprocess.run(["ip", "-o", "-f", "inet", "addr", "show"], capture_output=True, text=True)
            match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)/(\d+)", result.stdout)
            if match:
                return match.group(2)  # Return CIDR notation
    except Exception as e:
        print(f"{RED}Error getting subnet mask: {e}{RESET}")
    return None

def get_network_range():
    """Retrieve the CIDR network range from the local IP and subnet mask."""
    local_ip = get_local_ip()
    subnet_mask = get_subnet_mask()

    if not local_ip or not subnet_mask:
        print(f"{RED}Could not determine subnet mask!{RESET}")
        return []

    try:
        network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)
        return [str(ip) for ip in network.hosts()]
    except Exception as e:
        print(f"{RED}Error determining network range: {e}{RESET}")
        return []
