def gf2_rank():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Gaussian elimination over GF(2)
    rows = len(matrix)
    cols = len(matrix[0])
    
    current_row = 0
    
    for col in range(cols):
        # Find pivot
        pivot_row = -1
        for row in range(current_row, rows):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        
        if pivot_row == -1:
            continue
        
        # Swap rows
        matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]
        
        # Eliminate
        for row in range(rows):
            if row != current_row and matrix[row][col] == 1:
                for c in range(cols):
                    matrix[row][c] ^= matrix[current_row][c]
        
        current_row += 1
    
    # Count non-zero rows
    rank = 0
    for row in matrix:
        if any(val == 1 for val in row):
            rank += 1
    
    print(rank)

gf2_rank()