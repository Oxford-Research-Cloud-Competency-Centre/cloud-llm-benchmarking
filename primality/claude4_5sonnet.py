def miller_rabin(n, a):
    if n == a:
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return True
    
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    
    return False

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in witnesses:
        if a >= n:
            break
        if not miller_rabin(n, a):
            return False
    
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print("NEITHER")
    elif is_prime(N):
        print("PRIME")
    else:
        print("COMPOSITE")