def solve_sat(n, clauses):
    # Try all possible assignments using backtracking
    def backtrack(variable, assignment):
        if variable > n:
            # Check if current assignment satisfies all clauses
            for clause in clauses:
                satisfied = False
                for lit in clause:
                    if lit > 0:
                        if assignment[lit - 1] == 1:
                            satisfied = True
                            break
                    else:
                        if assignment[-lit - 1] == 0:
                            satisfied = True
                            break
                if not satisfied:
                    return False
            return True
        
        # Try assigning 0 to current variable
        assignment[variable - 1] = 0
        if backtrack(variable + 1, assignment):
            return True
        
        # Try assigning 1 to current variable
        assignment[variable - 1] = 1
        if backtrack(variable + 1, assignment):
            return True
        
        return False
    
    # Initialize assignment array
    assignment = [0] * n
    
    if backtrack(1, assignment):
        return assignment
    else:
        return None

# Read input
n, m = map(int, input().split())
clauses = []
for _ in range(m):
    line = list(map(int, input().split()))
    clause = line[:-1]  # Remove the trailing 0
    clauses.append(clause)

# Solve SAT
result = solve_sat(n, clauses)

if result is None:
    print("UNSAT")
else:
    print("SAT")
    print(" ".join(map(str, result)))