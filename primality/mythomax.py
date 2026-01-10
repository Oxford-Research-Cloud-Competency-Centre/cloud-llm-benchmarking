from functools import lru_cache
from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@lru_cache(maxsize=None)
def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0:
            return True
        i += 6
    return False

def solve(N):
    if N == 1:
        return "NEITHER"
    if N <= 2:
        return "PRIME"
    if is_prime(N):
        return "PRIME"
    if is_composite(N):
        return "COMPOSITE"
    else:
        return "NEITHER"

tests = [int(input()) for _ in range(5)]

for T, N in zip(tests, tests[1:]):
    print(solve(N))