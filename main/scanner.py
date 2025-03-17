import subprocess
import socket
import concurrent.futures
import os
from network_utils import get_network_range, GREEN, RED, CYAN, YELLOW, RESET

def ping(ip):
    """Ping an IP address to check if it's live (ICMP)."""
    try:
        cmd = ["ping", "-c", "1", "-W", "0.5", ip] if os.name != "nt" else ["ping", "-n", "1", "-w", "500", ip]
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return ip if result.returncode == 0 else None
    except:
        return None

def tcp_syn_scan(ip, port=80):
    """Perform a TCP SYN scan on the given IP and port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            return ip if result == 0 else None
    except:
        return None

def scan():
    """Scan the network using ICMP ping and TCP SYN."""
    network_ips = get_network_range()
    if not network_ips:
        print(f"{RED}No valid IPs found for scanning.{RESET}")
        return []

    active_hosts = []

    print(f"{CYAN}Scanning network...\n{RESET}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_results = {executor.submit(ping, ip): ip for ip in network_ips}
        
        for future in concurrent.futures.as_completed(future_results):
            result = future.result()
            if result:
                active_hosts.append(result)
                print(f"{GREEN}[LIVE] {result}{RESET}")

    if not active_hosts:
        print(f"{YELLOW}No hosts responded to ICMP ping. Trying TCP SYN scan...{RESET}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            future_results = {executor.submit(tcp_syn_scan, ip): ip for ip in network_ips}

            for future in concurrent.futures.as_completed(future_results):
                result = future.result()
                if result:
                    active_hosts.append(result)
                    print(f"{GREEN}[LIVE - TCP SYN] {result}{RESET}")

    return active_hosts
