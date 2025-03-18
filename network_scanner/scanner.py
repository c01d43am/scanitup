from utils.ip_utils import get_local_ip, get_scan_range
from utils.scan_utils import ping, arp_scan
import concurrent.futures

def scan():
    """Scan the network for active hosts using ping and ARP scan."""
    local_ip = get_local_ip()
    if not local_ip:
        print("Could not determine local IP address.")
        return

    scan_ranges = get_scan_range(local_ip)
    if not scan_ranges:
        print(f"Unsupported local IP range: {local_ip}")
        return

    print(f"Scanning network: {local_ip} (Full Range)\n")
    print("----------------------------------------------------\n")

    active_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        future_results = {executor.submit(ping, f"{subnet}{i}"): f"{subnet}{i}" for subnet in scan_ranges for i in range(1, 255)}
        
        for future in concurrent.futures.as_completed(future_results):
            result = future.result()
            if result:
                active_hosts.append(result)

    if active_hosts:
        print("\nActive Hosts Found:")
        print("---------------------------------")
        print("\n".join(active_hosts))
    else:
        print("\nNo active hosts found.")

    # Run ARP scan to detect all connected devices
    arp_scan()

if __name__ == "__main__":
    scan()
