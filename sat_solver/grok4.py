N, M = map(int, input().split())
clauses = []
for _ in range(M):
    line = list(map(int, input().split()))
    clauses.append(line[:-1])

found = False
satisfying_assign = None
for mask in range(1 << N):
    assign = [0] * (N + 1)
    for i in range(1, N + 1):
        if mask & (1 << (i - 1)):
            assign[i] = 1
    sat = True
    for clause in clauses:
        clause_sat = False
        for lit in clause:
            var = abs(lit)
            required = 1 if lit > 0 else 0
            if assign[var] == required:
                clause_sat = True
                break
        if not clause_sat:
            sat = False
            break
    if sat:
        found = True
        satisfying_assign = assign[1:]
        break

if found:
    print("SAT")
    print(' '.join(map(str, satisfying_assign)))
else:
    print("UNSAT")