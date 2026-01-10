import sys

def read_input():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return 0, 0, []
    n, m = map(int, data.split())
    clauses = []
    for line in data[1:1 + m]:
        nums = list(map(int, line.split()))
        clause = [x for x in nums if x != 0]
        clauses.append(clause)
    return n, m, clauses

def is_satisfied(clauses, assignment):
    # assignment: list of booleans, 1-based index (assignment[1..N])
    for clause in clauses:
        satisfied = False
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if lit > 0 and val:
                satisfied = True
                break
            if lit < 0 and not val:
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def main():
    n, m, clauses = read_input()
    if n == 0:
        print("UNSAT")
        return

    # brute-force over all assignments (N <= 20 => 2^20 = 1,048,576)
    for mask in range(1 << n):
        assignment = [False] * (n + 1)
        for i in range(1, n + 1):
            assignment[i] = bool((mask >> (i - 1)) & 1)
        if is_satisfied(clauses, assignment):
            print("SAT")
            vals = ['1' if assignment[i] else '0' for i in range(1, n + 1)]
            print(" ".join(vals))
            return

    print("UNSAT")

if __name__ == "__main__":
    main()