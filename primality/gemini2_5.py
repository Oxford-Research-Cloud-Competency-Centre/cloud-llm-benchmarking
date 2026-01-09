import sys

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0 or n % 3 == 0:
        return "COMPOSITE"

    # Bases for deterministic Miller-Rabin for n < 2^64
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        if a >= n:
            break
        
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue

        composite = True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = False
                break
        
        if composite:
            return "COMPOSITE"

    return "PRIME"

def main():
    input = sys.stdin.readline
    try:
        t_str = input()
        if not t_str.strip():
            return
        t = int(t_str)
        for _ in range(t):
            n_str = input()
            if not n_str.strip():
                continue
            n = int(n_str)
            print(is_prime(n))
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()