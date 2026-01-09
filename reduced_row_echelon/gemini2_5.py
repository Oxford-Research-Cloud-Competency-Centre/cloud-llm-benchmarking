import sys

def solve():
    try:
        n, m = map(int, sys.stdin.readline().split())
        cols = m + 1
        matrix = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().split()))
            matrix.append(row)
    except (IOError, ValueError):
        return

    rank = 0
    pivot_row = 0
    for col in range(cols):
        if pivot_row >= n:
            break
        
        i = pivot_row
        while i < n and matrix[i][col] == 0:
            i += 1
            
        if i