import random

def miller_rabin(n, k=5):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

def main():
    try:
        t = int(input().strip())
        for _ in range(t):
            try:
                n = int(input().strip())
                print(miller_rabin(n))
            except ValueError:
                # In a real application, you'd log this or handle it more robustly
                pass
    except ValueError:
        # In a real application, you'd log this or handle it more robustly
        pass

if __name__ == "__main__":
    main()