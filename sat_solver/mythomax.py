def sat_solver(formula):
    clauses = [list(map(int, clause.split(' ')) for clause in formula.split('\n') if clause]
    variables = set()
    for clause in clauses:
        for literal in clause:
            if literal > 0:
                variables.add(1)
            elif literal < 0:
                variables.add(-1)
    if len(variables) == 0:
        return "UNSAT"
    else:
        for var in range(1, N+1):
            if var not in variables:
                variables.add(var)
        return 'SAT\n'.join(["1" if literal == 1 else "0" for literal in variables])