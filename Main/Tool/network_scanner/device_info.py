import socket
import subprocess
import time

def get_mac(ip):
    """Retrieve MAC address of a given IP."""
    try:
        result = subprocess.run(["arp", "-a", ip], capture_output=True, text=True)
        lines = result.stdout.split("\n")
        for line in lines:
            if ip in line:
                parts = line.split()
                return parts[1] if len(parts) > 1 else "Unknown"
    except:
        return "Unknown"

def reverse_dns(ip):
    """Retrieve the hostname of a given IP."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def get_device_info(ip):
    """Return MAC, Hostname, and first seen time."""
    mac = get_mac(ip)
    hostname = reverse_dns(ip)
    return {"ip": ip, "mac": mac, "hostname": hostname, "first_seen": time.strftime("%H:%M:%S")}
