# Read input from standard input
input_line = input().strip()

# Split the input line into a list of strings and convert to integers
numbers = list(map(int, input_line.split()))

# Sort the list in ascending order
numbers.sort()

# Print the sorted list as space-separated values
print(' '.join(map(str, numbers)))