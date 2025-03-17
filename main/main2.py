# import socket
# import platform
# import subprocess
# import concurrent.futures
# import re

# # ANSI color codes
# RED = "\033[91m"
# GREEN = "\033[92m"
# CYAN = "\033[96m"
# RESET = "\033[0m"

# def get_local_ip():
#     """Retrieve the local IP address of the machine."""
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         local_ip = s.getsockname()[0]
#         s.close()
#         print(f"[DEBUG] Local IP Detected: {CYAN}{local_ip}{RESET}")
#         return local_ip
#     except Exception as e:
#         print(f"{RED}Error getting local IP: {e}{RESET}")
#         return None

# def get_scan_range(local_ip):
#     """Determine the network range based on the IP class."""
#     try:
#         octets = local_ip.split(".")
#         first_octet = int(octets[0])

#         if 0 <= first_octet <= 127:  # Class A (255.0.0.0)
#             print("[INFO] Class A network detected.")
#             return [f"{first_octet}.{i}.{j}." for i in range(256) for j in range(256)]
        
#         elif 128 <= first_octet <= 191:  # Class B (255.255.0.0)
#             print("[INFO] Class B network detected.")
#             return [f"{first_octet}.{octets[1]}.{i}." for i in range(256)]
        
#         elif 192 <= first_octet <= 223:  # Class C (255.255.255.0)
#             print("[INFO] Class C network detected.")
#             return [f"{first_octet}.{octets[1]}.{octets[2]}."]

#         elif 224 <= first_octet <= 239:  # Class D (Multicast)
#             print("[INFO] Class D network detected (Multicast).")
#             return [f"{first_octet}.{i}.{j}." for i in range(256) for j in range(256)]
        
#         elif 240 <= first_octet <= 255:  # Class E (Experimental)
#             print("[INFO] Class E network detected (Experimental).")
#             return [f"{first_octet}.{i}.{j}." for i in range(256) for j in range(256)]
        
#         else:
#             print("[ERROR] Unsupported IP class.")
#             return []
    
#     except Exception as e:
#         print(f"{RED}Error determining scan range: {e}{RESET}")
#         return []

# def ping(ip):
#     """Ping an IP address to check if it's live."""
#     try:
#         cmd = ["ping", "-c", "1", "-W", "0.5", ip] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "500", ip]
#         result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#         if result.returncode == 0:
#             print(f"{GREEN}[LIVE] {ip}{RESET}")
#             return ip
#     except Exception as e:
#         print(f"{RED}Error pinging {ip}: {e}{RESET}")
#     return None

# def arp_scan():
#     """Retrieve all IP and MAC addresses of connected devices using ARP."""
#     print("\n[INFO] Running ARP scan to detect all connected devices...\n")
#     devices = []
#     try:
#         if platform.system() == "Windows":
#             cmd = ["arp", "-a"]
#             result = subprocess.run(cmd, capture_output=True, text=True)
#             pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]+)", result.stdout)
#         else:
#             cmd = ["ip", "neigh"]
#             result = subprocess.run(cmd, capture_output=True, text=True)
#             pattern = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+.*\s+([a-fA-F0-9:-]+)", result.stdout)

#         if pattern:
#             print("Connected Devices:")
#             print("-----------------------------------------")
#             print(f"{CYAN}IP Address\t\tMAC Address{RESET}")
#             print("-----------------------------------------")
#             for ip, mac in pattern:
#                 devices.append((ip, mac))
#                 print(f"{GREEN}{ip}\t{mac}{RESET}")

#     except Exception as e:
#         print(f"{RED}Error performing ARP scan: {e}{RESET}")
    
#     return devices

# def scan():
#     """Scan the network for active hosts using ping and ARP scan."""
#     local_ip = get_local_ip()
#     if not local_ip:
#         print("Could not determine local IP address.")
#         return

#     scan_ranges = get_scan_range(local_ip)
#     if not scan_ranges:
#         print(f"Unsupported local IP range: {local_ip}")
#         return

#     print(f"Scanning network: {local_ip} (Full Range)\n")
#     print("----------------------------------------------------\n")

#     active_hosts = []

#     with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
#         future_results = {executor.submit(ping, f"{subnet}{i}"): f"{subnet}{i}" for subnet in scan_ranges for i in range(1, 255)}
        
#         for future in concurrent.futures.as_completed(future_results):
#             result = future.result()
#             if result:
#                 active_hosts.append(result)

#     if active_hosts:
#         print("\nActive Hosts Found:")
#         print("---------------------------------")
#         print("\n".join(active_hosts))
#     else:
#         print("\nNo active hosts found.")

#     # Run ARP scan to detect all connected devices
#     arp_scan()

# if __name__ == "__main__":
#     scan()
# print("")
