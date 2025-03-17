from scanner import scan
from device_info import arp_scan
import datetime

def main():
    print("Starting network scan...\n")
    
    active_hosts = scan()
    arp_devices = arp_scan()

    print("\nActive Hosts Found:")
    print("---------------------------------")
    for host in active_hosts:
        print(f"IP: {host}")

    print("\nConnected Devices (From ARP Scan):")
    print("---------------------------------")
    for device in arp_devices:
        connection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Connected at: {connection_time}")

if __name__ == "__main__":
    main()
