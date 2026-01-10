def is_partial_assignment_valid(assignment, clauses):
    for clause in clauses:
        clause_satisfied = False
        all_assigned = True
        for var, sign in clause:
            idx = var - 1
            if assignment[idx] is None:
                all_assigned = False
                break
            value = assignment[idx]
            if (value == 1 and sign) or (value == 0 and not sign):
                clause_satisfied = True
                break
        if not clause_satisfied and all_assigned:
            return False
    return True

def select_variable(assignment):
    for i in range(len(assignment)):
        if assignment[i] is None:
            return i + 1
    return None

def backtrack(assignment, clauses, N):
    if None not in assignment:
        return assignment.copy()
    var = select_variable(assignment)
    if var is None:
        return None
    for value in [0, 1]:
        new_assignment = assignment.copy()
        new_assignment[var-1] = value
        if not is_partial_assignment_valid(new_assignment, clauses):
            continue
        result = backtrack(new_assignment, clauses, N)
        if result is not None:
            return result
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2
    clauses = []
    for _ in range(M):
        clause = []
        while data[idx]!= '0':
            lit = int(data[idx])
            clause.append(lit)
            idx += 1
        idx += 1  # skip the '0'
        processed = []
        for lit in clause:
            if lit > 0:
                processed.append((lit, True))
            else:
                processed.append((-lit, False))
        clauses.append(processed)
    
    assignment = [None] * N
    result = backtrack(assignment, clauses, N)
    
    if result is not None:
        print("SAT")
        print(' '.join(map(str, result)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()