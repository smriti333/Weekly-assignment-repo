import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()

        if content1 == content2:
            print("The files are the same.")
        else:
            print("The files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        compare_files(sys.argv[1], sys.argv[2])
