# File Reading Example

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

read_file("example.txt")

input("\nPress ENTER to exit...")
