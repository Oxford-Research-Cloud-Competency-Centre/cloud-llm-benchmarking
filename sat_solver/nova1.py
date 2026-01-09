def sat_solver(N, M, clauses):
    def backtrack(var_assignment):
        if len(var_assignment) == N:
            if all(evaluate_clause(clause, var_assignment) for clause in clauses):
                return var_assignment
            else:
                return None

        for value in [0, 1]:
            new_assignment = var_assignment + [value]
            result = backtrack(new_assignment)
            if result is not None:
                return result
        return None

    def evaluate_clause(clause, assignment):
        return any(clause[i] > 0 and assignment[abs(clause[i]) - 1] == 1 or
                   clause[i] < 0 and assignment[abs(clause[i]) - 1] == 0
                   for i in range(len(clause) - 1))

    result_assignment = backtrack([])
    if result_assignment:
        print("SAT")
        print(" ".join(map(str, result_assignment)))
    else:
        print("UNSAT")

# Example usage
N, M = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(M)]
sat_solver(N, M, clauses)