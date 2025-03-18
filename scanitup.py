import subprocess

def main():
    # Run design.py (Banner & Version Display)
    subprocess.run(["python", "Design/design.py"], check=True)

    # Run index.py (Main Menu)
    subprocess.run(["python", "Index/index.py"], check=True)

if __name__ == "__main__":
    main()
