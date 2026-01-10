def sat_solver(n, m, clauses):
    def dpll(assignment, clauses):
        if not clauses:
            return assignment
        for clause in clauses:
            if not clause:
                return None
        unit_clauses = [clause for clause in clauses if len(clause) == 1]
        if unit_clauses:
            unit_clause = unit_clauses[0][0]
            new_assignment = assignment.copy()
            new_assignment[abs(unit_clause)] = 1 if unit_clause > 0 else 0
            new_clauses = [c for c in clauses if unit_clause not in c]
            new_clauses = [[literal for literal in c if literal != -unit_clause] for c in new_clauses]
            return dpll(new_assignment, new_clauses)
        pure_literals = []
        for var in range(1, n + 1):
            positive_count = sum(1 for clause in clauses for literal in clause if literal == var)
            negative_count = sum(1 for clause in clauses for literal in clause if literal == -var)
            if positive_count > 0 and negative_count == 0:
                pure_literals.append(var)
            elif positive_count == 0 and negative_count > 0:
                pure_literals.append(-var)
        if pure_literals:
            pure_literal = pure_literals[0]
            new_assignment = assignment.copy()
            new_assignment[abs(pure_literal)] = 1 if pure_literal > 0 else 0
            new_clauses = [c for c in clauses if pure_literal not in c]
            new_clauses = [[literal for literal in c if literal != -pure_literal] for c in new_clauses]
            return dpll(new_assignment, new_clauses)
        var = next((abs(literal) for clause in clauses for literal in clause if abs(literal) not in assignment), None)
        if var is None:
            return assignment
        for val in [1, 0]:
            new_assignment = assignment.copy()
            new_assignment[var] = val
            new_clauses = [c[:] for c in clauses]
            literal = var if val == 1 else -var
            new_clauses = [c for c in new_clauses if literal not in c]
            new_clauses = [[l for l in c if l != -literal] for c in new_clauses]
            result = dpll(new_assignment, new_clauses)
            if result is not None:
                return result
        return None

    assignment = {i: None for i in range(1, n + 1)}
    result = dpll(assignment, clauses)
    if result is None:
        return "UNSAT"
    else:
        sat_assignment = [result[i] for i in range(1, n + 1)]
        return "SAT\n" + " ".join(map(str, sat_assignment))


def main():
    try:
        n, m = map(int, input().split())
        clauses = []
        for _ in range(m):
            clause = list(map(int, input().split()))
            clause = clause[:-1]  # Remove the trailing 0
            clauses.append(clause)
        print(sat_solver(n, m, clauses))
    except EOFError:
        pass


if __name__ == "__main__":
    main()