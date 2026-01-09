import math

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

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    
    def trial_composite(a):
        if pow(a, s, n) == 1:
            return False
        for _ in range(r - 1):
            if pow(a, s * (2 ** _), n) == n - 1:
                return False
        return True
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if trial_composite(a):
            return False
    return True

def solve(t, test_cases):
    results = []
    for n in test_cases:
        if n == 1:
            results.append("NEITHER")
        elif n < 4 * (10 ** 6):
            results.append("PRIME" if is_prime(n) else "COMPOSITE")
        else:
            results.append("PRIME" if miller_rabin(n) else "COMPOSITE")
    return results

import random
T = int(input())
test_cases = [int(input()) for _ in range(T)]
results = solve(T, test_cases)
for result in results:
    print(result)