import socket
from ..Design.constants import RED, CYAN, RESET  # Use absolute import

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"[DEBUG] Local IP Detected: {CYAN}{local_ip}{RESET}")
        return local_ip
    except Exception as e:
        print(f"{RED}Error getting local IP: {e}{RESET}")
        return None
