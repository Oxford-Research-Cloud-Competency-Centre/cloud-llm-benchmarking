def gaussian_elimination_gf2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rank = 0
    
    for col in range(cols):
        # Find pivot row
        pivot_row = -1
        for r in range(rank, rows):
            if matrix[r][col] == 1:
                pivot_row = r
                break
        
        if pivot_row == -1:
            continue  # No pivot in this column
        
        # Swap pivot row with current rank row
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        
        # Eliminate this column in all other rows
        for r in range(rows):
            if r != rank and matrix[r][col] == 1:
                for c in range(cols):
                    matrix[r][c] ^= matrix[rank][c]
        
        rank += 1
    
    return rank

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Compute rank using Gaussian elimination over GF(2)
rank = gaussian_elimination_gf2(matrix)

# Output the rank
print(rank)