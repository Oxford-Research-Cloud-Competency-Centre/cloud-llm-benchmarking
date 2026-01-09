import sys

nums = list(map(int, sys.stdin.read().split()))
nums.sort()
print(' '.join(map(str, nums)))