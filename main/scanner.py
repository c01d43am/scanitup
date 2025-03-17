import platform
import subprocess
import concurrent.futures
from network_utils import get_local_ip, get_scan_range

def ping(ip):
    """Ping an IP address to check if it's live."""
    try:
        cmd = ["ping", "-c", "1", "-W", "0.5", ip] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "500", ip]
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            return ip
    except:
        pass
    return None

def scan():
    """Scan the network for active hosts using ping."""
    local_ip = get_local_ip()
    if not local_ip:
        print("Could not determine local IP address.")
        return

    scan_ranges = get_scan_range(local_ip)
    if not scan_ranges:
        print(f"Unsupported local IP range: {local_ip}")
        return

    active_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        future_results = {executor.submit(ping, f"{subnet}{i}"): f"{subnet}{i}" for subnet in scan_ranges for i in range(1, 255)}
        
        for future in concurrent.futures.as_completed(future_results):
            result = future.result()
            if result:
                active_hosts.append(result)

    return active_hosts
