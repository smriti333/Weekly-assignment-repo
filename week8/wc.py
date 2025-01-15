import sys

def wc(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)
            
            print(f"Lines: {num_lines}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <file_name>")
    else:
        wc(sys.argv[1])
