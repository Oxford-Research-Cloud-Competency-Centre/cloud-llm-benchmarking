def is_satisfiable(N, M, clauses):
    # Backtracking solver for SAT problem
    def backtrack(assignment):
        # Check if all clauses are satisfied
        if all(any((lit > 0 and assignment[abs(lit) - 1] is True) or (lit < 0 and assignment[abs(lit) - 1] is False) for lit in clause) for clause in clauses):
            return True
        
        # Find the first unassigned variable
        for i in range(N):
            if assignment[i] is None:
                break
        else:
            return False
        
        # Try assigning True to the variable
        assignment[i] = True
        if backtrack(assignment):
            return True
        
        # Try assigning False to the variable
        assignment[i] = False
        if backtrack(assignment):
            return True
        
        # Backtrack
        assignment[i] = None
        return False
    
    # Initialize assignment list with None
    assignment = [None] * N
    
    # Start backtracking
    if backtrack(assignment):
        print("SAT")
        print(" ".join("1" if val else "0" for val in assignment))
    else:
        print("UNSAT")

# Read input
import sys
input = sys.stdin.read
data = input().split()
index = 0

N = int(data[index])
index += 1
M = int(data[index])
index += 1

clauses = []
for _ in range(M):
    clause = []
    while True:
        x = int(data[index])
        index += 1
        if x == 0:
            break
        clause.append(x)
    clauses.append(clause)

# Solve the SAT problem
is_satisfiable(N, M, clauses)