def matrix_rank_gf2(N, M, matrix):
    rank = 0
    rows = N
    cols = M + 1
    
    for i in range(rows):
        if i >= rank:
            j = i
            while j < rows and matrix[j][i] == 0:
                j += 1
            if j == rows:
                continue
            
            matrix[i], matrix[j] = matrix[j], matrix[i]
            
            for k in range(i + 1, rows):
                xor_row = [matrix[k][l] ^ matrix[i][l] for l in range(cols)]
                matrix[k] = xor_row
            
            for k in range(rows):
                if k!= i and matrix[k][i] == 1:
                    for l in range(i, cols):
                        matrix[k][l] ^= matrix[i][l]
            
            rank += 1
    
    return rank

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
index = 2
matrix = []

for _ in range(N):
    row = [int(data[index + i]) for i in range(M + 1)]
    matrix.append(row)
    index += M + 1

# Calculate rank
result = matrix_rank_gf2(N, M, matrix)
print(result)