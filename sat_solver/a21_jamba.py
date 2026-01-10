def satisfies_clause(clause, assignment):
    for lit in clause:
        if lit > 0 and assignment[lit - 1] == 1:
            return True
        if lit < 0 and assignment[-lit - 1] == 0:
            return True
    return False

def sat_solver(n, m, clauses):
    for assignment in range(2**n):
        var_assignment = [((assignment >> i) & 1) for i in range(n)]
        if all(satisfies_clause(clause, var_assignment) for clause in clauses):
            return var_assignment
    return None

def main():
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split()[:-1])) for _ in range(m)]
    result = sat_solver(n, m, clauses)
    if result is None:
        print("UNSAT")
    else:
        print("SAT")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()