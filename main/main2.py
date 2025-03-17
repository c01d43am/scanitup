import socket
import platform
import subprocess
import concurrent.futures

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return None

def get_scan_range(local_ip):
    """Determine the IP range to scan based on the local network class."""
    if local_ip.startswith("10."):
        return [f"10.{i}.{j}." for i in range(256) for j in range(256)]  # Class A
    elif local_ip.startswith("172.") and 16 <= int(local_ip.split(".")[1]) <= 31:
        return [f"172.{i}.{j}." for i in range(16, 32) for j in range(256)]  # Class B
    elif local_ip.startswith("192.168."):
        return [f"192.168.{i}." for i in range(256)]  # Class C
    elif local_ip.startswith("224."):
        return [f"224.{i}.{j}." for i in range(256) for j in range(256)]  # Class D (Multicast)
    elif local_ip.startswith("240."):
        return [f"240.{i}.{j}." for i in range(256) for j in range(256)]  # Class E (Experimental)
    else:
        return []

def ping(ip):
    """Ping an IP address and return its status."""
    cmd = ["ping", "-c", "1", "-W", "0.1", ip] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "100", ip]
    
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if result.returncode == 0:
        print(f"{GREEN}[LIVE] {ip}{RESET}")
        return ip
    else:
        print(f"{RED}[DEAD] {ip}{RESET}", end="\r")
        return None

def scan():
    """Scan the local network for active hosts."""
    local_ip = get_local_ip()
    if not local_ip:
        print("Could not determine local IP address.")
        return

    scan_ranges = get_scan_range(local_ip)

    if not scan_ranges:
        print(f"Unsupported local IP range: {local_ip}")
        return

    print(f"Scanning network based on local IP: {local_ip}...\n")
    print("----------------------------------------------------\n")

    active_hosts = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_results = {executor.submit(ping, f"{subnet}{i}"): f"{subnet}{i}" for subnet in scan_ranges for i in range(1, 255)}
        
        for future in concurrent.futures.as_completed(future_results):
            result = future.result()
            if result:
                active_hosts.append(result)

    if active_hosts:
        print("\nActive Hosts Found:")
        print("\n---------------------------------")
        print("\n".join(active_hosts))
    else:
        print("\nNo active hosts found.")

scan()
