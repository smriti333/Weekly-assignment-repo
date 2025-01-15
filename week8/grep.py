import sys

def grep(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if pattern in line:
                    print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <file_name>")
    else:
        grep(sys.argv[1], sys.argv[2])
