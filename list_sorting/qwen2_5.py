# Read the input line, split into parts, convert to integers
numbers = list(map(int, input().strip().split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted list as space-separated values
print(' '.join(map(str, numbers)))