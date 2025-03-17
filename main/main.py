from network_utils import get_local_ip, get_scan_range
from scanner import network_scan, arp_scan

# ANSI color codes
RED = "\033[91m"
RESET = "\033[0m"

def main():
    """Main execution flow."""
    local_ip = get_local_ip()
    if not local_ip:
        print(f"{RED}[ERROR] Could not determine local IP. Exiting.{RESET}")
        return

    scan_ranges = get_scan_range(local_ip)
    if not scan_ranges:
        print(f"[ERROR] Unsupported local IP range: {local_ip}. Exiting.")
        return

    # Perform network scan using ping
    network_scan(scan_ranges)

    # Perform ARP scan to detect connected devices
    arp_scan()

if __name__ == "__main__":
    main()
