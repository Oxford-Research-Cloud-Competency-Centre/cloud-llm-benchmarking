def read_input():
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause[:-1])  # Remove the trailing 0
    return n, m, clauses

def evaluate_clause(clause, assignment):
    for literal in clause:
        var = abs(literal)
        value = assignment[var - 1]
        if literal > 0 and value == 1:
            return True
        if literal < 0 and value == 0:
            return True
    return False

def evaluate_formula(clauses, assignment):
    for clause in clauses:
        if not evaluate_clause(clause, assignment):
            return False
    return True

def solve_sat(n, clauses):
    # Try all possible assignments (2^n possibilities)
    for i in range(2**n):
        assignment = []
        for j in range(n):
            assignment.append((i >> j) & 1)
        
        if evaluate_formula(clauses, assignment):
            return assignment
    
    return None

def main():
    n, m, clauses = read_input()
    solution = solve_sat(n, clauses)
    
    if solution:
        print("SAT")
        print(' '.join(map(str, solution)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()