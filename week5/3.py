import sys

def find_shortest_argument(arguments):
    return sorted(arguments, key=len)[0]

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments:
        shortest_argument = find_shortest_argument(arguments)
        print(shortest_argument)