def matrix_rank(N, M, matrix):
    # Convert matrix to reduced row echelon form (RREF) using Gaussian elimination
    for i in range(N):
        # Find the pivot row
        pivot_row = i
        for j in range(i + 1, N):
            if matrix[j][i] == 1:
                pivot_row = j
                break
        # Swap rows if needed
        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
        # Eliminate entries in the same column below the pivot
        for j in range(i + 1, N):
            if matrix[j][i] == 1:
                for k in range(i, M + 1):
                    matrix[j][k] = matrix[j][k] ^ matrix[i][k]
    # Count non-zero rows to get the rank
    rank = sum(1 for row in matrix if any(cell == 1 for cell in row))
    return rank

def main():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    rank = matrix_rank(N, M, matrix)
    print(rank)

if __name__ == "__main__":
    main()