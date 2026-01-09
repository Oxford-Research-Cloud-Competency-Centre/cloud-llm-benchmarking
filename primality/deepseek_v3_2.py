import sys
import random

def power_mod(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        d = d // 2
        a = (a * a) % n
    return result

def miller_rabin(n, k=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n % p == 0:
            return "COMPOSITE" if n != p else "PRIME"
    
    if miller_rabin(n):
        return "PRIME"
    else:
        return "COMPOSITE"

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        n = int(input_data[i])
        results.append(is_prime(n))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()