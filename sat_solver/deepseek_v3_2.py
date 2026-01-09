import sys

def solve_sat(N, M, clauses):
    def evaluate_assignment(assignment):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                val = assignment[var-1]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    def backtrack(idx, assignment):
        if idx == N:
            return evaluate_assignment(assignment)
        for val in [0, 1]:
            assignment[idx] = val
            if backtrack(idx + 1, assignment):
                return True
        assignment[idx] = 0
        return False
    
    assignment = [0] * N
    if backtrack(0, assignment):
        print("SAT")
        print(" ".join(str(x) for x in assignment))
        return True
    else:
        print("UNSAT")
        return False

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    N, M = map(int, data[0].split())
    clauses = []
    for i in range(1, M+1):
        literals = list(map(int, data[i].split()))[:-1]
        clauses.append(literals)
    solve_sat(N, M, clauses)

if __name__ == "__main__":
    main()