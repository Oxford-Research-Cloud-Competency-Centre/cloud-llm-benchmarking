def mod2_rank(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rank = 0

    for row in range(n):
        # Find the first non-zero column in the current row
        pivot_col = None
        for col in range(m):
            if matrix[row][col] == 1:
                pivot_col = col
                break

        if pivot_col is None:
            continue

        # Swap rows to move the pivot to the current row
        if row != pivot_col:
            matrix[row], matrix[pivot_col] = matrix[pivot_col], matrix[row]

        # Reduce the column below the pivot
        for i in range(row + 1, n):
            if matrix[i][row] == 1:
                matrix[i] = [(x ^ y) for x, y in zip(matrix[i], matrix[row])]

        rank += 1

    return rank

def parse_input():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix

def main():
    matrix = parse_input()
    rank = mod2_rank(matrix)
    print(rank)

if __name__ == "__main__":
    main()