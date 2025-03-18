import platform
import subprocess
import threading
import ipaddress
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import device_info  # Importing device_info.py

def get_local_ip():
    """Get the local IP address."""
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        return next((line.split(":")[-1].strip() for line in result.stdout.split("\n") if "IPv4 Address" in line), None)
    else:
        result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
        return result.stdout.strip().split()[0]

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

def scan_network_live():
    """Perform a live scan and call device_info.py for details."""
    scan_range = calculate_cidr()
    if not scan_range:
        return

    total_ips = len(scan_range)
    found_devices = []
    scanned_count = 0

    print("[🔍] Scanning network live... Press Ctrl+C to stop.\n")
    time.sleep(1)

    def worker(ip):
        nonlocal scanned_count
        scanned_count += 1
        result = ping_host(ip)
        if result:
            device_details = device_info.get_device_info(ip)  # Call device_info.py
            found_devices.append(device_details)
            print(f"\r[✅] Found: {device_details['ip']} | MAC: {device_details['mac']} | Name: {device_details['hostname']}                      ")

        sys.stdout.write(f"\r[⏳] Scanning... {scanned_count}/{total_ips} IPs checked")
        sys.stdout.flush()

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(worker, ip): ip for ip in scan_range}
        try:
            for future in futures:
                future.result()  # Wait for each thread to complete
        except KeyboardInterrupt:
            print("\n[⚠] Scan interrupted. Exiting...")

    print("\n[✅] Scan Complete!")
    if found_devices:
        print("\n[🔎] Active Devices Found:")
        for device in found_devices:
            print(f"  → {device['ip']} | MAC: {device['mac']} | Name: {device['hostname']}")
    else:
        print("\n[❌] No active devices found.")

if __name__ == "__main__":
    scan_network_live()
