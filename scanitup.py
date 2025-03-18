# Import the required modules
import sys
import time
import subprocess
from Main.Tool.Design.design import Font_banner
from Main.Index.index import main as index_main
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Function to display a loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(3):
        for char in animation:
            sys.stdout.write(f"\rLoading... {char} ")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rLoading... done!       \n")
    sys.stdout.flush()
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Function to display an "exploitation" animation
def exploitation_animation():
    exploit_text = [
        "Yummy...",
        "Exploiting...",
    ]
    for text in exploit_text:
        sys.stdout.write(f"\r{text}    ")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nExploit successful!")
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Function to check for updates from GitHub
def check_for_updates():
    print("\nChecking for updates from the GitHub repository...")
    try:
        result = subprocess.run(["git", "pull", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("GitHub repository is up-to-date.")
        else:
            print(f"Failed to update the repository: {result.stderr.strip()}")
    except Exception as e:
        print(f"Error checking for updates: {e}")
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Main execution function
def main():
    Font_banner()  # Display banner
    check_for_updates()  # Check for updates
    loading_animation()  # Show loading animation
    exploitation_animation()  # Display exploitation animation
    index_main()  # Execute index main function

if __name__ == "__main__":
    main()
