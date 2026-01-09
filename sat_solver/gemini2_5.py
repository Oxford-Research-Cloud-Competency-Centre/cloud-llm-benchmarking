import sys

def solve():
    """
    Solves the SAT problem by iterating through all possible assignments.
    This is a brute-force approach, feasible for N <= 20.
    """
    line = sys.stdin.readline()
    if not line:
        return
        
    try:
        n_str, m_str = line.split()
        n = int(n_str)
        m = int(m_str)
    except (ValueError, IndexError):
        print("UNSAT")
        return

    clauses = []
    for _ in range(m):
        try:
            clause = list(map(