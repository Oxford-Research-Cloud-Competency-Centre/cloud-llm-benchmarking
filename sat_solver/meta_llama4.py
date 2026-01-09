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
            literal = unit_clause if unit_clause > 0 else -unit_clause
            value = 1 if unit_clause > 0 else 0
            new_assignment = assignment.copy()
            new_assignment[literal] = value
            new_clauses = simplify_clauses(clauses, unit_clause)
            result = dpll(new_assignment, new_clauses)
            if result is not None:
                return result
            else:
                return None
        else:
            literal = abs(clauses[0][0])
            for value in [1, 0]:
                new_assignment = assignment.copy()
                new_assignment[literal] = value
                new_clauses = simplify_clauses(clauses, literal if value == 1 else -literal)
                result = dpll(new_assignment, new_clauses)
                if result is not None:
                    return result
            return None

    def simplify_clauses(clauses, literal):
        new_clauses = []
        for clause in clauses:
            new_clause = [l for l in clause if l != literal]
            if -literal not in new_clause:
                new_clauses.append(new_clause)
        return new_clauses

    assignment = {i: None for i in range(1, n+1)}
    result = dpll(assignment, clauses)
    if result is None:
        return "UNSAT"
    else:
        sat_assignment = [int(result[i]) for i in range(1, n+1)]
        return "SAT\n" + " ".join(map(str, sat_assignment))

def main():
    try:
        n, m = map(int, input().split())
        clauses = []
        for _ in range(m):
            clause = list(map(int, input().split()))
            clause = clause[:-1]
            clauses.append(clause)
        print(sat_solver(n, m, clauses))
    except EOFError:
        pass

if __name__ == "__main__":
    main()