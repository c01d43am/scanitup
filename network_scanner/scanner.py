import platform
import subprocess
import threading
import ipaddress

def get_local_ip():
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    else:
        result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
    return result.stdout.strip().split()[0]

def calculate_cidr(ip, prefix="/24"):
    network = ipaddress.ip_network(f"{ip}{prefix}", strict=False)
    return [str(host) for host in network.hosts()]

def ping_host(ip):
    system = platform.system()
    cmd = ["ping", "-n", "1", ip] if system == "Windows" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    return ip if "TTL=" in result.stdout else None

def scan_network():
    local_ip = get_local_ip()
    scan_range = calculate_cidr(local_ip)
    results = []
    
    def worker(ip):
        if ping_host(ip):
            results.append(ip)
    
    threads = []
    for ip in scan_range:
        t = threading.Thread(target=worker, args=(ip,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    return results
