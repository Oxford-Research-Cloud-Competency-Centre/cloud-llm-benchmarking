def gaussian_elimination(matrix, n, m):
    rank = 0
    for col in range(m):
        pivot = -1
        for row in range(rank, n):
            if matrix[row][col] == 1:
                pivot = row
                break
        if pivot == -1:
            continue
        matrix[pivot], matrix[rank] = matrix[rank], matrix[pivot]
        for row in range(n):
            if row != rank and matrix[row][col] == 1:
                for j in range(col, m + 1):
                    matrix[row][j] = (matrix[row][j] + matrix[rank][j]) % 2
        rank += 1
    return rank

def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    rank = gaussian_elimination(matrix, n, m)
    print(rank)

if __name__ == "__main__":
    main()