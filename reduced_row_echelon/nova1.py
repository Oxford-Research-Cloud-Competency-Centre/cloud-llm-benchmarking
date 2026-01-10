def matrix_rank_gf2(n, m, equations):
    matrix = [list(map(int, eq.split())) for eq in equations]
    rank = 0
    row = 0

    for col in range(m):
        while row < n and all(matrix[row][col] == 0 for row in range(row, n)):
            col += 1
            if col == m:
                break
        if row == n:
            break
        rank += 1
        for i in range(row + 1, n):
            if matrix[i][col] == 1:
                matrix[i] = [a ^ b for a, b in zip(matrix[i], matrix[row])]
        row += 1

    return rank

# Example usage
n, m = 3, 3
equations = [
    "1 0 1 1",
    "0 1 1 0",
    "1 1 0 1"
]
print(matrix_rank_gf2(n, m, equations))