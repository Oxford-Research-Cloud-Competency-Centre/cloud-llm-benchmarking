def evaluate_clause(clause, assignment):
    for lit in clause:
        var = abs(lit)
        val = assignment[var - 1]
        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
            return True
    return False

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        if not evaluate_clause(clause, assignment):
            return False
    return True

def solve_sat(n, clauses):
    for i in range(2**n):
        assignment = [0] * n
        temp = i
        for j in range(n):
            assignment[j] = temp % 2
            temp //= 2
        if is_satisfiable(clauses, assignment):
            return True, assignment
    return False, None

def main():
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clause.pop()  # Remove the trailing 0
        clauses.append(clause)
    
    satisfiable, assignment = solve_sat(n, clauses)
    
    if satisfiable:
        print("SAT")
        print(" ".join(map(str, assignment)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()