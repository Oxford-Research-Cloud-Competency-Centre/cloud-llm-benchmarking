import sys

def main():
    data = sys.stdin.read().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        n = int(data[index])
        index += 1
        if n == 1:
            print("NEITHER")
            continue
        if n == 2 or n == 3:
            print("PRIME")
            continue
        if n % 2 == 0 or n % 3 == 0:
            print("COMPOSITE")
            continue
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        witnesses = [2, 3, 5, 7, 11, 13, 23, 29, 31]
        is_composite = False
        for a in witnesses:
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            continue_r = False
            for r in range(1, s):
                x = (x * x) % n
                if x == n - 1:
                    continue_r = True
                    break
            if continue_r:
                continue
            is_composite = True
            break
        if is_composite:
            print("COMPOSITE")
        else:
            print("PRIME")

if __name__ == "__main__":
    main()