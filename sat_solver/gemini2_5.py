import sys

def solve():
    """
    Main function to read input, run the SAT solver, and print the output.
    """
    try:
        line1 = sys.stdin.readline()
        if not line1.strip():
            print("UNSAT")
            return
        n, m = map(int, line1.split())
        
        clauses = []
        for _ in range(m):
            line = sys.stdin.readline()
            if not line.strip():
                continue
            literals = list(map(int, line.split()))[:-1]
            if literals:
                clauses.append(literals)

    except (ValueError, IndexError):
        print("UNSAT")
        return

    assignment = [-1] * n
    
    solution = find_satisfying_assignment(clauses, assignment, 0, n)

    if solution:
        print("SAT")
        print(*solution)
    else:
        print("UNSAT")

def find_satisfying_assignment(clauses, assignment, var_index, n):
    """
    Recursively finds a satisfying assignment using a backtracking algorithm.
    
    Args:
        clauses: The list of clauses in CNF.
        assignment: The current partial assignment of variables (0, 1, or -1 for unassigned).
        var_index: The index of the variable to assign next (0 to n-1).
        n: The total number of variables.

    Returns:
        A list representing the satisfying assignment if found, otherwise None.
    """
    if var_index == n:
        return assignment[:]

    # Try assigning the current variable to 0 (False)
    assignment[var_index] = 0
    if is_consistent(clauses, assignment):
        result = find_satisfying_assignment(clauses, assignment, var_index + 1, n)
        if result is not None:
            return result

    # Backtrack and try assigning the current variable to 1 (True)
    assignment[var_index] = 1
    if is_consistent(clauses, assignment):
        result = find_satisfying_assignment(clauses, assignment, var_index + 1, n)
        if result is not None:
            return result
    
    # Backtrack: un-assign the variable for parent recursive calls
    assignment[var_index] = -1
    
    return None

def is_consistent(clauses, assignment):
    """
    Checks if a partial assignment is consistent (i.e., does not make any clause false).
    A clause is false only if all of its literals are assigned and evaluate to false.
    
    Args:
        clauses: The list of clauses in CNF.
        assignment: The current partial assignment.

    Returns:
        True if the assignment is consistent, False otherwise.
    """
    for clause in clauses:
        is_satisfied = False
        all_literals_resolved = True
        
        for literal in clause:
            var_num = abs(literal)
            var_idx = var_num - 1
            
            value = assignment[var_idx]
            
            if value == -1:
                all_literals_resolved = False
                continue

            if (literal > 0 and value == 1) or (literal < 0 and value == 0):
                is_satisfied = True
                break
        
        if not is_satisfied and all_literals_resolved:
            return False
            
    return True

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    solve()