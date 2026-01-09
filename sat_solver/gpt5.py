import sys

def apply_assignment(clauses, var, value):
    new_clauses = []
    sat_lit = var if value else -var
    rem_lit = -var if value else var
    for clause in clauses:
        satisfied = False
        new_clause = []
        for lit in clause:
            if lit == sat_lit:
                satisfied = True
                break
            elif lit == rem_lit:
                continue
            else:
                new_clause.append(lit)
        if satisfied:
            continue
        if not new_clause:
            return None
        new_clauses.append(new_clause)
    return new_clauses

def dpll(clauses, assignment):
    while True:
        units = [c[0] for c in clauses if len(c) == 1]
        if units:
            for lit in units:
                v = abs(lit)
                val = lit > 0
                if v in assignment and assignment[v] != val:
                    return None
                assignment[v] = val
                clauses = apply_assignment(clauses, v, val)
                if clauses is None:
                    return None
            continue

        pos = set()
        neg = set()
        for c in clauses:
            for lit in c:
                if lit > 0:
                    pos.add(lit)
                else:
                    neg.add(-lit)
        pures = []
        for v in pos:
            if v not in neg and v not in assignment:
                pures.append((v, True))
        for v in neg:
            if v not in pos and v not in assignment:
                pures.append((v, False))
        if pures:
            for v, val in pures:
                assignment[v] = val
                clauses = apply_assignment(clauses, v, val)
                if clauses is None:
                    return None
            continue
        break

    if not clauses:
        return assignment

    lit = None
    for c in clauses:
        if c:
            lit = c[0]
            break
    if lit is None:
        return assignment
    v = abs(lit)

    for val in (True, False):
        new_assignment = assignment.copy()
        new_assignment[v] = val
        new_clauses = apply_assignment(clauses, v, val)
        if new_clauses is None:
            continue
        res = dpll(new_clauses, new_assignment)
        if res is not None:
            return res
    return None

def solve_sat(N, clauses):
    assignment = {}
    res = dpll(clauses, assignment)
    return res

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    it = iter(tokens)
    N = int(next(it))
    M = int(next(it))
    clauses = []
    current = []
    count = 0
    for t in it:
        x = int(t)
        if x == 0:
            clauses.append(current)
            current = []
            count += 1
            if count == M:
                break
        else:
            current.append(x)

    result = solve_sat(N, clauses)
    if result is None:
        print("UNSAT")
    else:
        print("SAT")
        print(' '.join('1' if result.get(i, False) else '0' for i in range(1, N + 1)))

if __name__ == "__main__":
    main()