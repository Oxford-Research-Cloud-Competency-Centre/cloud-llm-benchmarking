import sys

def rank_gf2(matrix, n, m):
    rank = 0
    col = 0
    for row in range(n):
        if col >= m + 1:
            break
        pivot = row
        while pivot < n and matrix[pivot][col] == 0:
            pivot += 1
        if pivot == n:
            col += 1
            row -= 1
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        pivot_row = matrix[row]
        for r in range(n):
            if r != row and matrix[r][col] == 1:
                for c in range(col, m + 1):
                    matrix[r][c] ^= pivot_row[c]
        rank += 1
        col += 1
    return rank

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = map(int, data[:2])
    matrix = []
    idx = 2
    for _ in range(n):
        row = list(map(int, data[idx:idx + m + 1]))
        matrix.append(row)
        idx += m + 1
    rank = rank_gf2(matrix, n, m)
    print(rank)

if __name__ == "__main__":
    main()