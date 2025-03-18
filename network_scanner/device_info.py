import socket
import time
import subprocess

def get_mac(ip):
    try:
        result = subprocess.run(["arp", "-a", ip], capture_output=True, text=True)
        lines = result.stdout.split("\n")
        for line in lines:
            if ip in line:
                return line.split()[1]
    except:
        return "Unknown"

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def get_device_info(ips):
    devices = []
    for ip in ips:
        mac = get_mac(ip)
        hostname = reverse_dns(ip)
        devices.append({"ip": ip, "mac": mac, "hostname": hostname, "first_seen": time.strftime("%H:%M:%S")})
    return devices
