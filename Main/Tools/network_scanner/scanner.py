#--------------------------------------------------------------------------------------------------------------------------------------------------------
import platform
import subprocess
import ipaddress
import sys
import time
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from Main.Tools.network_scanner.device_info import get_device_info

def get_local_ip():
    """Get the local IP address."""
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        return next((line.split(":")[-1].strip() for line in result.stdout.split("\n") if "IPv4 Address" in line), None)
    else:
        result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
        return result.stdout.strip().split()[0]

def get_mac_address(ip):
    """Get the MAC address of a given IP."""
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["arp", "-a", ip], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if ip in line:
                return line.split()[1]
    else:
        result = subprocess.run(["arp", "-n", ip], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if ip in line:
                return line.split()[2]
    return "Unknown"

def get_cidr():
    """Determine network CIDR dynamically."""
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        ip = next((line.split(":")[-1].strip() for line in result.stdout.split("\n") if "IPv4 Address" in line), None)
        mask = next((line.split(":")[-1].strip() for line in result.stdout.split("\n") if "Subnet Mask" in line), None)
        if ip and mask:
            cidr = sum(bin(int(x)).count("1") for x in mask.split("."))
            return f"{ip}/{cidr}"
    else:
        result = subprocess.run(["ip", "-o", "-f", "inet", "addr", "show"], capture_output=True, text=True)
        match = next((line.split()[3] for line in result.stdout.split("\n") if "inet" in line), None)
        return match
    return None

def calculate_cidr():
    """Generate IP list in the network range."""
    cidr = get_cidr()
    if not cidr:
        print("[❌] Could not determine network range!")
        return []
    network = ipaddress.ip_network(cidr, strict=False)
    return [str(host) for host in network.hosts()]

def ping_host(ip):
    """Ping a host and check if it's online."""
    system = platform.system()
    cmd = ["ping", "-n", "1", ip] if system == "Windows" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    
    if system == "Windows":
        return ip if "TTL=" in result.stdout else None
    else:
        return ip if "bytes from" in result.stdout else None

def scan_network_live(silent_mode=False, output_file=None):
    """Perform a live scan and call device_info.py for details."""
    scan_range = calculate_cidr()
    if not scan_range:
        return

    total_ips = len(scan_range)
    found_devices = []
    scanned_count = 0

    if not silent_mode:
        print("\n[🔍] Scanning network live... Press Ctrl+C to stop.\n")
    time.sleep(1)

    def worker(ip):
        nonlocal scanned_count
        scanned_count += 1
        result = ping_host(ip)
        if result:
            device_details = get_device_info(ip)
            device_details['mac'] = get_mac_address(ip)  # Retrieve MAC address
            device_details['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            found_devices.append(device_details)
            if not silent_mode:
                print(f"\n[✅] Found: {device_details['ip']} | MAC: {device_details['mac']} | Name: {device_details['hostname']} | Time: {device_details['timestamp']}")
        
        if not silent_mode:
            sys.stdout.write(f"\r[⏳] Scanning... {scanned_count}/{total_ips} IPs checked")
            sys.stdout.flush()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(worker, ip): ip for ip in scan_range}
        try:
            for future in futures:
                future.result()  # Wait for each thread to complete
        except KeyboardInterrupt:
            print("\n[⚠] Scan interrupted. Exiting...")
    
    print("\n\n[✅] Scan Complete!")
    if found_devices:
        print("\n[🔎] Active Devices Found:")
        for device in found_devices:
            print(f"  → {device['ip']} | MAC: {device['mac']} | Name: {device['hostname']} | Time: {device['timestamp']}")
    else:
        print("\n[❌] No active devices found.")
    
    if output_file:
        with open(output_file, "w") as f:
            json.dump(found_devices, f, indent=4)
        print(f"[💾] Scan results saved to {output_file}")

if __name__ == "__main__":
    scan_network_live(silent_mode=False, output_file="scan_results.json")
