import sys

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        skip = False
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                skip = True
                break
        if skip:
            continue
        return False
    return True

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    t = data[0]
    nums = data[1:1 + t]
    out_lines = []
    for n in nums:
        if n == 1:
            out_lines.append("NEITHER")
        else:
            out_lines.append("PRIME" if is_prime(n) else "COMPOSITE")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()