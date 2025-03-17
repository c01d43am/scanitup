import socket
import platform

# ANSI color codes
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"[DEBUG] Local IP Detected: {CYAN}{local_ip}{RESET}")
        return local_ip
    except Exception as e:
        print(f"{RED}Error getting local IP: {e}{RESET}")
        return None

def get_scan_range(local_ip):
    """Determine the network range based on the IP class."""
    try:
        octets = local_ip.split(".")
        first_octet = int(octets[0])

        if 0 <= first_octet <= 127:  # Class A (255.0.0.0)
            print("[INFO] Class A network detected.")
            return [f"{first_octet}.{i}.{j}." for i in range(256) for j in range(256)]
        
        elif 128 <= first_octet <= 191:  # Class B (255.255.0.0)
            print("[INFO] Class B network detected.")
            return [f"{first_octet}.{octets[1]}.{i}." for i in range(256)]
        
        elif 192 <= first_octet <= 223:  # Class C (255.255.255.0)
            print("[INFO] Class C network detected.")
            return [f"{first_octet}.{octets[1]}.{octets[2]}."]

        else:
            print("[ERROR] Unsupported IP class.")
            return []
    
    except Exception as e:
        print(f"{RED}Error determining scan range: {e}{RESET}")
        return []
