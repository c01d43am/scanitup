# Import the required modules
from Working.Tool.Design.design import Font_banner
from Working.Index.index import main as index_main

def main():
    Font_banner()  # Call banner display function first
    index_main()   # Call index.py main function

if __name__ == "__main__":
    main()
