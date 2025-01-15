import sys
import platform

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--platform':
        os_platform = platform.system()
        print(f"The operating system platform is: {os_platform}")
    else:
        print("Usage: python script.py --platform")

if __name__ == "__main__":
    main()