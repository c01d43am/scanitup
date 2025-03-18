import sys
import os
import random

# Ensure correct module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Tool')))

# Use absolute imports
from Tools.network_scanner.scanner import scan_network
from Tools.network_scanner.device_info import get_device_info
from Tools.network_scanner.output import display_results

def main():
    while True:
        try:
            print("\n📡 Network Scanner - Main Menu")
            print("1️⃣  Run Network Scan")
            print("2️⃣  Show Connected Devices")
            print("3️⃣  Exit")

            choice = input("🔹 Enter your choice: ").strip()

            if choice == "1":
                print("\n🔍 Starting Network Scan...")
                scan_results = scan_network()
                if not scan_results:
                    print("⚠ No active devices found.")
                else:
                    detailed_results = get_device_info(scan_results)
                    display_results(detailed_results)

            elif choice == "2":
                print("\n📡 Connected Devices:")
                scan_results = scan_network()
                if not scan_results:
                    print("⚠ No connected devices found.")
                else:
                    connected_devices = get_device_info(scan_results)
                    display_results(connected_devices)

            elif choice == "3":
                print("🚪 Exiting... Goodbye!")
                sys.exit(0)

            else:
                funny_responses = [
                    "Oops! That wasn't on the menu. Try again! 🚫",
                    "Nice try, but that's not an option! 😜",
                    "Invalid choice. Are you testing my patience? 🤨",
                    "Error 404: Your choice not found! 🤖",
                    "You broke the menu... Just kidding, try again! 😂"
                ]
                print(random.choice(funny_responses))

        except KeyboardInterrupt:
            print("\n[!] KeyboardInterrupt detected. Exiting gracefully... 👋")
            sys.exit(0)

if __name__ == "__main__":
    main()
