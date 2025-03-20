import socket
import subprocess
import datetime
import concurrent.futures
import requests

def check_ip(ip):
    """Check if an IP is alive by pinging it."""    
    try:
        subprocess.run(["ping", "-n", "1", "-w", "10", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)   # Windows
        return True
    except subprocess.CalledProcessError:   # ping returns non-zero exit code
        return False

def get_hostname(ip):
    """Retrieve the hostname of an IP."""
    try:
        return socket.gethostbyaddr(ip)[0]  # Reverse DNS lookup
    except socket.herror:  # No hostname found
        return "Unknown"    

def get_mac(ip):  
    """Retrieve the MAC address of an IP.""" 
    try:   
        output = subprocess.check_output(["arp", "-a"], shell=True).decode() # Windows 
        for line in output.split("\n"): 
            parts = line.split() 
            if len(parts) >= 2 and parts[0] == ip: 
                return parts[1]
    except:
        return "Unknown"
    return "Unknown"

def scan_ip(ip):
    """Scan a single IP address."""
    is_alive = check_ip(ip)
    if is_alive:
        status = "🟢 Active"
        hostname = get_hostname(ip)
        mac_address = get_mac(ip)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
        print(f"{ip:<16} {status:<10} {hostname:<18} {mac_address:<20} {timestamp}") 
        return {"ip": ip, "hostname": hostname, "mac": mac_address, "timestamp": timestamp} 
    return None 

def scan_network(ip_range):
    """Scan a range of IP addresses using multithreading."""
    print("\nScanning for connected devices...\n")
    print("IP Address        Status       Hostname          MAC Address          Timestamp")
    print("-" * 80)
    
    devices = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(scan_ip, ip_range))
    
    for device in results:
        if device:
            devices.append(device)
    
    return devices

def get_public_ip():
    """Retrieve the public IP of the network."""
    try:
        response = requests.get("https://api64.ipify.org?format=text", timeout=5)
        return response.text
    except requests.RequestException:
        return "Unknown"

def get_local_gateway():
    """Retrieve the default gateway IP."""
    try:
        result = subprocess.check_output("ipconfig", shell=True).decode()
        for line in result.split("\n"):
            if "Default Gateway" in line:
                return line.split()[-1]
    except:
        return "Unknown"
    return "Unknown"

def get_connected_devices():
    """Retrieve the list of connected devices using ARP."""
    try:
        output = subprocess.check_output(["arp", "-a"], shell=True).decode()
        devices = []
        for line in output.split("\n"):
            parts = line.split()
            if len(parts) >= 2 and "." in parts[0]:
                devices.append({"ip": parts[0], "mac": parts[1]})
        return devices
    except:
        return []

if __name__ == "__main__":
    public_ip = get_public_ip()
    gateway_ip = get_local_gateway()
    
    print(f"Public IP Address: {public_ip}")
    print(f"Local Network Gateway: {gateway_ip}\n")
    
    connected_devices = get_connected_devices()
    print("Connected Devices:")
    print("IP Address        MAC Address")
    print("-" * 40)
    for device in connected_devices:
        print(f"{device['ip']:<16} {device['mac']:<20}")
    
    private_ranges = [
        ("10.0.0.1", "10.255.255.254"),
        ("172.16.0.1", "172.31.255.254"),
        ("192.168.0.1", "192.168.255.254")
    ]
    
    for start, end in private_ranges:
        print(f"\nScanning range {start} to {end}\n")
        ip_range = [device['ip'] for device in connected_devices]
        scan_network(ip_range)
    
    print("\nScan complete.")
