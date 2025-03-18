import sys
from Design.constants import Font_banner
import Design  # Import design module

def main():
    Design.run()  # Run design script before menu
    
    while True:
        print("\nChoose an option:")
        print("1. Run Network Scan")
        print("2. Show Connected Devices")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            ()
        elif choice == "2":
            ()
        elif choice == "3":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()