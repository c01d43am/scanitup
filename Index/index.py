import sys
import os
from ..network_scanner.scanner import scan_network
from ..network_scanner.device_info import get_device_info
from ..network_scanner.output import display_results

def main():

    while True:
        print("\nChoose an option:")
        print("1. Run Network Scan")
        print("2. Show Connected Devices")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n🔍 Starting Network Scan...")
            scan_results = scan_network()
            detailed_results = get_device_info(scan_results)
            display_results(detailed_results)
        elif choice == "2":
            print("\n📡 Connected Devices:")
            scan_results = scan_network()
            connected_devices = get_device_info(scan_results)
            display_results(connected_devices)
        elif choice == "3":
            print("🚪 Exiting...")
            sys.exit(0)
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
