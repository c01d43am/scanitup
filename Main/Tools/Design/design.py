import random
from . import banner_art
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ANSI escape codes for colors
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
reset = "\033[0m"  # Reset color
green = "\033[32m"  # Green color

def Font_banner():
    color = random.choice(colors)  # Pick a random color
    banner = banner_art.get_banner()  # Get a random banner
    print(f"{color}{banner}{reset}")

    # Display version & author at the bottom
    version = f"{green}\t\t\tv0.0.1 by c01d43am{reset}"
    print("\t\thttps://github.com/c01d43am")
    print(f"\n{version}\n")

# Call function for testing
if __name__ == "__main__":
    Font_banner()
