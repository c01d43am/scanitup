# Import the required modules
from Main.Tool.Design.design import Font_banner
from Main.Index.index import main as index_main

def main():
    Font_banner()  # Call banner display function first
    index_main()   # Call index.py main function

if __name__ == "__main__":
    main()
