import sys
import random

def is_prime(n):
    if n <= 1:
        return False, "NEITHER"
    if n <= 3:
        return True, "PRIME"
    if n % 2 == 0 or n % 3 == 0:
        return False, "COMPOSITE"
    
    # Miller-Rabin test with deterministic bases for numbers up to 2^64
    # Using the deterministic set of bases: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # This is sufficient for all numbers up to 2^64
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Deterministic bases for numbers < 2^64
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in bases:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False, "COMPOSITE"
    
    return True, "PRIME"

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        prime, result = is_prime(N)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()