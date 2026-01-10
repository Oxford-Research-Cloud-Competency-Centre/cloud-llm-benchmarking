from math import sqrt
from random import randint

def miller_rabin(n, k=5):
    if n <= 1 or n == 4:
        return "COMPOSITE"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    # Find r such that n − 1 = 2^s * r with r odd
    r = n - 1
    s = 0
    while r % 2 == 0:
        r //= 2
        s += 1
    
    # Perform k rounds of Miller-Rabin test
    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, r, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

def is_prime(n):
    if n == 1:
        return "NEITHER"
    return miller_rabin(n)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(is_prime(N))

if __name__ == "__main__":
    main()