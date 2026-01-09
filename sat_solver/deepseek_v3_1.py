def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print("UNSAT")
        return
        
    first_line = data[0].split()
    n = int(first_line[0])
    m = int(first_line[1])
    
    clauses = []
    for i in range(1, m+1):
        parts = list(map(int, data[i].split()))
        clause = parts[:-1]
        clauses.append(clause)
    
    from itertools import product
    for assignment in product([0, 1], repeat=n):
        assignment_list = list(assignment)
        satisfied = True
        for clause in clauses:
            clause_sat = False
            for lit in clause:
                var = abs(lit)
                sign = 1 if lit > 0 else 0
                if assignment_list[var-1] == sign:
                    clause_sat = True
                    break
            if not clause_sat:
                satisfied = False
                break
        if satisfied:
            print("SAT")
            print(" ".join(str(x) for x in assignment_list))
            return
            
    print("UNSAT")

if __name__ == "__main__":
    main()