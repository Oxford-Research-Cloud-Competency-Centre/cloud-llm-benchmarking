import sys

try:
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers.sort()
    print(*numbers)
except (ValueError, IndexError):
    pass