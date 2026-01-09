import random

def miller_rabin(n, k=5):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n == 2:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    if miller_rabin(n):
        return "PRIME"
    else:
        return "COMPOSITE"

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_prime(n))