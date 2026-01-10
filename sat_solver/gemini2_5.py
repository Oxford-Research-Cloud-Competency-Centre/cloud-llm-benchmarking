import sys

def solve():
    """
    Solves the SAT problem by iterating through all possible variable assignments.
    """
    try:
        line = sys.stdin.readline()
        if not line.strip():
            return
        N, M = map(int, line.split())
    except (IOError, ValueError):
        return

    # Reading clauses from standard input
    clauses = []
    for _ in range(M):
        literals = list(map(int, sys.stdin.readline().strip().split()))[:-1]
        clauses.append(literals)

    # Pre-process clauses into bitmasks for faster evaluation.
    # For each clause, we create a mask for positive literals and one for negative ones.
    processed_clauses = []
    for clause in clauses:
        pos_mask = 0
        neg_mask = 0
        for literal in clause:
            # Variables are 1-indexed, so we use abs(literal) - 1 for 0-indexed bit position.
            var_index = abs(literal) - 1
            if literal > 0:
                pos_mask |= (1 << var_index)
            else:
                neg_mask |= (1 << var_index)
        processed_clauses.append((pos_mask, neg_mask))

    # Iterate through all 2^N possible assignments.
    # Each integer 'i' from 0 to 2^N - 1 represents a unique assignment.
    # The j-th bit of 'i' corresponds to the truth value of variable j+1.
    for i in range(1 << N):
        assignment_satisfies_all = True
        for pos_mask, neg_mask in processed_clauses:
            # A clause is satisfied if at least one of its literals is true.
            
            # Check if any positive literal is satisfied.
            # A positive literal x_k is true if variable k is true (k-th bit of i is 1).
            # This is true if the assignment 'i' has at least one '1' bit in common with pos_mask.
            positive_part_satisfied = (i & pos_mask) != 0
            
            # Check if any negative literal is satisfied.
            # A negative literal not(x_k) is true if variable k is false (k-th bit of i is 0).
            # This is true if the assignment 'i' is missing at least one '1' bit that neg_mask has.
            # If (i & neg_mask) == neg_mask, it means all corresponding variables are true,
            # so all negative literals in this part are false.
            negative_part_satisfied = (i & neg_mask) != neg_mask

            if not (positive_part_satisfied or negative_part_satisfied):
                assignment_satisfies_all = False
                break
        
        if assignment_satisfies_all:
            print("SAT")
            # Construct the assignment list (0s and 1s) from the integer 'i'.
            assignment = [(i >> j) & 1 for j in range(N)]
            print(*assignment)
            return

    # If the loop completes without finding a solution, the formula is unsatisfiable.
    print("UNSAT")

if __name__ == "__main__":
    solve()