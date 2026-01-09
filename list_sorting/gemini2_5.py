import sys

try:
    input_line = sys.stdin.readline()
    if input_line.strip():
        numbers = list(map(int, input_line.split()))
        numbers.sort()
        print(*numbers)
except (ValueError, IndexError):
    pass