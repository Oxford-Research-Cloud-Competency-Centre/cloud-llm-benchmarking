import math

def is_prime(n):
    if n <= 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0 or n % 3 == 0:
        return "COMPOSITE"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "COMPOSITE"
        i += 6
    return "PRIME"

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if witness(a):
            return False
    return True

def is_prime_large(n, k=5):
    if n <= 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0 or n % 3 == 0:
        return "COMPOSITE"
    
    if n <= 10**6:
        return is_prime(n)
    
    if miller_rabin(n, k):
        return "PRIME"
    return "COMPOSITE"

import random
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
output = []

for i in range(1, T + 1):
    N = int(data[i])
    if N <= 10**6:
        output.append(is_prime(N))
    else:
        output.append(is_prime_large(N))

print("\n".join(output))