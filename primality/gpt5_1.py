import sys

def is_prime(n: int) -> bool:
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

    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out_lines = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            out_lines.append("NEITHER")
        elif is_prime(n):
            out_lines.append("PRIME")
        else:
            out_lines.append("COMPOSITE")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()