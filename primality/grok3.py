def mod_pow(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    temp = mod_pow(base, exp // 2, mod)
    if exp % 2 == 0:
        return (temp * temp) % mod
    else:
        return (((temp * temp) % mod) * base) % mod

def miller_rabin_test(a, d, n, r):
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
        if x == 1:
            return False
    return False

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a >= n:
            break
        if not miller_rabin_test(a, d, n, r):
            return False
    return True

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N == 1:
            print("NEITHER")
        elif is_prime(N):
            print("PRIME")
        else:
            print("COMPOSITE")

if __name__ == "__main__":
    solve()