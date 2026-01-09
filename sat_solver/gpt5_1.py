import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    clauses = []
    for _ in range(M):
        pos = 0
        neg = 0
        while True:
            x = int(next(it))
            if x == 0:
                break
            if x > 0:
                pos |= 1 << (x - 1)
            else:
                neg |= 1 << ((-x) - 1)
        clauses.append((pos, neg))
    full_mask = (1 << N) - 1
    for a in range(1 << N):
        sat = True
        for pos, neg in clauses:
            if not ((a & pos) or ((~a) & neg & full_mask)):
                sat = False
                break
        if sat:
            assignment = [str(1 if (a >> i) & 1 else 0) for i in range(N)]
            sys.stdout.write("SAT\n")
            sys.stdout.write(" ".join(assignment))
            return
    sys.stdout.write("UNSAT")

if __name__ == "__main__":
    main()