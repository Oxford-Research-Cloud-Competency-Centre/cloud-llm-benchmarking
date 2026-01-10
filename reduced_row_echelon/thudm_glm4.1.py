n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rank = 0
for col in range(m + 1):  # m+1 columns (variables + constants)
    # Find pivot row
    pivot_row = -1
    for row in range(rank, n):
        if matrix[row][col] == 1:
            pivot_row = row
            break
    if pivot_row == -1:
        continue  # no pivot in this column
    
    # Swap pivot row with current row (rank)
    if pivot_row != rank:
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
    
    # Make all other rows in this column 0
    for row in range(n):
        if row != pivot_row and matrix[row][col] == 1:
            for k in range(m + 1):
                matrix[row][k] ^= matrix[pivot_row][k]
    
    rank += 1

print(rank)