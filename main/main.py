from scanner import scan
from device_info import arp_scan
import datetime
from network_utils import CYAN, GREEN, RESET, YELLOW

def main():
    print(f"{CYAN}Starting network scan...\n{RESET}")
    
    active_hosts = scan()
    arp_devices = arp_scan()

    print(f"\n{CYAN}Active Hosts Found:{RESET}")
    print("---------------------------------")
    for host in active_hosts:
        print(f"{GREEN}IP: {host}{RESET}")

    print(f"\n{CYAN}Connected Devices (From ARP Scan):{RESET}")
    print("-------------------------------------------------")
    for device in arp_devices:
        connection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{GREEN}IP: {device['ip']}, MAC: {device['mac']}, Name: {device['name']}, Connected at: {YELLOW}{connection_time}{RESET}")

if __name__ == "__main__":
    main()
