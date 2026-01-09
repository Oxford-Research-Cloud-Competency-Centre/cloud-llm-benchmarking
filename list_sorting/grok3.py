import sys

input_line = sys.stdin.readline().strip()
numbers = list(map(int, input_line.split()))
numbers.sort()
output = ' '.join(map(str, numbers))
print(output)