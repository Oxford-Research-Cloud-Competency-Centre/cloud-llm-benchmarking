import sys

def main():
    data = sys.stdin.read().strip().split('\n')
    if not data:
        print("UNSAT")
        return
        
    first_line = data[0].split()
    if len(first_line) < 2:
        print("UNSAT")
        return
        
    try:
        n = int(first_line[0])
        m = int(first_line[1])
    except:
        print("UNSAT")
        return
        
    if n < 1 or n > 20 or m < 1 or m > 100:
        print("UNSAT")
        return
        
    clauses = []
    for i in range(1, m + 1):
        line = data[i].strip()
        if not line:
            print("UNSAT")
            return
            
        parts = list(map(int, line.split()))
        if not parts or parts[-1] != 0:
            print("UNSAT")
            return
            
        clause = []
        for x in parts[:-1]:
            if x == 0:
                continue
            try:
                val = int(x)
                if val < -n or val > n:
                    print("UNSAT")
                    return
                clause.append(val)
            except:
                print("UNSAT")
                return
        if not clause:
            print("UNSAT")
            return
            
        clauses.append(clause)
    
    assignment = [0] * n

    def is_satisfied(clause):
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if lit > 0:
                if val == 1:
                    return True
            else:
                if val == 0:
                    return True
        return False

    def solve(index):
        if index == n:
            return all(is_satisfied(clause) for clause in clauses)
            
        assignment[index] = 0
        if solve(index + 1):
            return True
            
        assignment[index] = 1
        if solve(index + 1):
            return True
            
        return False

    if solve(0):
        print("SAT")
        print(' '.join(map(str, assignment)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()