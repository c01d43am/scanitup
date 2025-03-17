import socket

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

def get_scan_range(local_ip):
    """Determine the network range based on the IP class."""
    octets = local_ip.split(".")
    first_octet = int(octets[0])

    if 0 <= first_octet <= 127:  
        return [f"{first_octet}.{i}.{j}." for i in range(256) for j in range(256)]
    elif 128 <= first_octet <= 191:  
        return [f"{first_octet}.{octets[1]}.{i}." for i in range(256)]
    elif 192 <= first_octet <= 223:  
        return [f"{first_octet}.{octets[1]}.{octets[2]}."]

    return []
