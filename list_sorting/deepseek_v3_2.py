import sys

def main():
    # Read a line from standard input
    line = sys.stdin.readline().strip()
    
    # If the line is empty, print nothing
    if not line:
        return
    
    # Split the line into a list of strings and convert to integers
    numbers = list(map(int, line.split()))
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Convert back to strings and join with spaces
    result = ' '.join(map(str, numbers))
    
    # Print the sorted list
    print(result)

if __name__ == "__main__":
    main()