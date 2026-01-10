def matrix_rank(N, M, matrix):
    rank = 0
    for col in range(M + 1):
        pivot = None
        for row in range(rank, N):
            if matrix[row][col] == 1:
                pivot = row
                break
        if pivot is not None:
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            for row in range(pivot + 1, N):
                if matrix[row][col] == 1:
                    matrix[row] = [matrix[row][i] ^ matrix[rank][i] for i in range(M + 1)]
            rank += 1
    return rank

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix_rank(N, M, matrix))