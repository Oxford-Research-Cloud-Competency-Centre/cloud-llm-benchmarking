def solve_sat(N, M, clauses):
    variables = [0] * N
    while True:
        satisfied = True
        for clause in clauses:
            if not any(variables[abs(x) - 1] ^ (x < 0) for x in clause[:-1]):
                satisfied = False
                break

        if satisfied:
            print("SAT")
            print(*variables)
            break

        for i in range(N):
            variables[i] = 1 - variables[i]

        if variables[0] == 0:
            print("UNSAT")
            break

if __name__ == "__main__":
    N, M = map(int, input().split())
    clauses = []
    for _ in range(M):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    solve_sat(N, M, clauses)