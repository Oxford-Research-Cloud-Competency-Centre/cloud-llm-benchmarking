import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    M = int(data[ptr])
    ptr += 1
    clauses = []
    for _ in range(M):
        clause = []
        while True:
            lit = int(data[ptr])
            ptr += 1
            if lit == 0:
                break
            clause.append(lit)
        clauses.append(clause)
    
    preprocessed = []
    for clause in clauses:
        pc = []
        for lit in clause:
            var = abs(lit)
            mask = 1 << (var - 1)
            is_pos = lit > 0
            pc.append((mask, is_pos))
        preprocessed.append(pc)
    
    total = 1 << N
    for x in range(total):
        all_ok = True
        for clause in preprocessed:
            if not any((x & mask) if is_pos else ((x & mask) == 0) for (mask, is_pos) in clause):
                all_ok = False
                break
        if all_ok:
            assignment = [( (x >> (i - 1)) & 1 ) for i in range(1, N + 1)]
            print("SAT")
            print(' '.join(map(str, assignment)))
            return
    print("UNSAT")

if __name__ == "__main__":
    main()