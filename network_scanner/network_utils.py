# network_utils.py

import ipaddress

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_network_range():
    """Get the network range using CIDR notation."""
    try:
        ip_network = ipaddress.ip_network("192.168.1.0/24", strict=False)  # Replace with actual network
        return [str(ip) for ip in ip_network.hosts()]
    except ValueError:
        print(f"{RED}Invalid network range!{RESET}")
        return []

def ping(ip):
    """Ping an IP address to check if it's live."""
    import subprocess
    import platform

    try:
        cmd = ["ping", "-c", "1", "-W", "0.5", ip] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "500", ip]
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"{GREEN}[LIVE] {ip}{RESET}")
            return ip
    except Exception as e:
        print(f"{RED}Error pinging {ip}: {e}{RESET}")
    return None
