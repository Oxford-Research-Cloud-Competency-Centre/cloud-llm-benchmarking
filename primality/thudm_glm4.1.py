import sys

def get_d_s(N):
    if N == 1:
        return 0, 0
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    return d, s

def power_mod(a, d, N):
    result = 1
    a = a % N
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % N
        a = (a * a) % N
        d = d // 2
    return result

def miller_rabin_test(N, a):
    if N <= 1:
        return False
    d, s = get_d_s(N)
    if d == 0:
        return True  # N is 1 (handled earlier)
    a = a % N
    if a == 0 or a == 1:
        return False
    x = power_mod(a, d, N)
    if x == 1 or x == N - 1:
        return True
    for _ in range(s - 1):
        x = (x * x) % N
        if x == N - 1:
            return True
    return False

def is_prime(N):
    if N == 1:
        return "NEITHER"
    if N <= 3:
        return "PRIME"
    if N % 2 == 0:
        return "COMPOSITE"
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if N < 2**64:
        # Deterministic tests for numbers <= 2^64
        if N <= 1373653:
            for a in bases:
                if not miller_rabin_test(N, a):
                    return "COMPOSITE"
        elif N <= 25326001:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3):
                return "COMPOSITE"
        elif N <= 118670087467:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3) and not miller_rabin_test(N, 5):
                return "COMPOSITE"
        elif N <= 13268691:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3) and not miller_rabin_test(N, 5) and not miller_rabin_test(N, 7):
                return "COMPOSITE"
        elif N <= 2152302898747:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3) and not miller_rabin_test(N, 5) and not miller_rabin_test(N, 7) and not miller_rabin_test(N, 11):
                return "COMPOSITE"
        elif N <= 3474749660383:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3) and not miller_rabin_test(N, 5) and not miller_rabin_test(N, 7) and not miller_rabin_test(N, 11) and not miller_rabin_test(N, 13):
                return "COMPOSITE"
        elif N <= 341550071728321:
            if not miller_rabin_test(N, 2) and not miller_rabin_test(N, 3) and not miller_rabin_test(N, 5) and not miller_rabin_test(N, 7) and not miller_rabin_test(N, 11) and not miller_rabin_test(N, 13) and not miller_rabin_test(N, 17):
                return "COMPOSITE"
        else:
            for a in bases:
                if not miller_rabin_test(N, a):
                    return "COMPOSITE"
    else:
        # Probabilistic test for numbers > 2^64
        for a in bases:
            if not miller_rabin_test(N, a):
                return "COMPOSITE"
    return "PRIME"

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(is_prime(N))