import sys

data = sys.stdin.read().strip()
if data:
    nums = list(map(int, data.split()))
    nums.sort()
    print(" ".join(map(str, nums)))