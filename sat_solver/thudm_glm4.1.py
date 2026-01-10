def solve_sat(N, M, clauses):
    assignment = [False] * (N + 1)  # 1-based indexing
    
    if backtrack(1, assignment, clauses):
        result = [1 if x else 0 for x in assignment[1:]]
        return "SAT\n" + " ".join(map(str, result))
    else:
        return "UNSAT"

def backtrack(var, assignment, clauses):
    if var > N:
        return check_satisfiability(assignment, clauses)
    
    # Try both assignments
    assignment[var] = False
    if backtrack(var + 1, assignment, clauses):
        return True
    
    assignment[var] = True
    if backtrack(var + 1, assignment, clauses):
        return True
    
    # Backtrack
    assignment[var] = False
    return False

def check_satisfiability(assignment, clauses):
    for clause in clauses:
        satisfied = False
        for literal in clause[:-1]:  # exclude trailing 0
            if literal > 0:
                if assignment[abs(literal)]:
                    satisfied = True
                    break
            else:
                if not assignment[abs(literal)]:
                    satisfied = True
                    break
        if not satisfied:
            return False
    return True