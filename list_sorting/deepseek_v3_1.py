import sys

data = sys.stdin.readline().strip()
numbers = list(map(int, data.split()))
numbers.sort()
print(' '.join(map(str, numbers)))