import sys

sys.setrecursionlimit(200005)

def solve():
    """
    This function reads a graph, computes the number of Strongly Connected Components
    using Kosaraju's algorithm, and prints the result.
    """
    input = sys.stdin.readline

    try:
        line = input().strip()
        if not line:
            print(0)
            return
        N