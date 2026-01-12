def rank_of_matrix_over_gf(N, M, matrix):
    def xor(a, b):
        return a ^ b

    def row_add(row, row):
        return [xor(row[i], row[i]) for i in range(M + )]

    for i in range(N):
        if matrix[i][i] == :
            for j in range(i + , N):
                if matrix[j][i] == :
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        if matrix[i][i] == :
            for j in range(N):
                if j != i and matrix[j][i] == :
                    matrix[j] = row_add(matrix[j], matrix[i])

    rank = 
    for row in matrix:
        if any(row):
            rank += 

    return rank

# Read input
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the rank
print(rank_of_matrix_over_gf(N, M, matrix))