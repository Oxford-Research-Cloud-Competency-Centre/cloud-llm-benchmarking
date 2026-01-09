import sys

# Read input line and split into integers
numbers = list(map(int, sys.stdin.readline().split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted numbers space-separated
print(' '.join(map(str, numbers)))